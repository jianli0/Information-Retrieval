import sys
import ast
import math

class Solution:
    def __init__(self,file1,file2):
        self.resultFile = file1
        self.relevanceFile = file2
        self.output = []
        self.relevance = {}

        # three queries (each with 100 retrived files)
        self.totalResult = 300

        # deal with querys
        self.queryIDs = [12,13,19]
        self.queryMap = {12:1, 13:2, 19:3}

        # deal with ndcgs
        self.DcgTable = [0]
        self.ideaDcgTable = [0]
        self.ndcgTable = []

        # deal with p20
        self.p20 = []

        # deal with average precision query
        self.avg = {1:[], 2:[], 3:[]}


        # read the resultFile from homework3
        with open(self.resultFile) as f:
            lines = f.read().split("\n")

        for i in range(self.totalResult):
            element = lines[i].split()
            self.output.append([element[0], element[3], element[2], element[4], None, None, None, None])
        #  print self.output
        #  [queryID, Rank, Document ID, Document score, Relevance level, Precision, Recall, NDCG]
        #  [['1', '3127', '1', '14.404766'] ]

        #read relevanceFile
        with open(self.relevanceFile) as f:
            lines = f.read().split("\n")
            for i in lines:
                element = i.split()
                queryid = ast.literal_eval(element[0])
                if queryid in self.queryIDs:
                    mapid = self.queryMap[queryid]
                    if mapid in self.relevance.keys():
                        self.relevance[mapid].append(ast.literal_eval(element[2][5:]))
                    else:
                        self.relevance[mapid] = [ast.literal_eval(element[2][5:])]
        #  print self.relevance
        #  {1: [1523, 2080, 2246, 2629, 3127]}

    def precision(self, doc, relevantNum):
        return relevantNum * 1.0 / ast.literal_eval(doc[1])

    def recall(self, doc, relevantNum, relevantTotal):
        return relevantNum * 1.0 / relevantTotal

    def ndcg(self, doc,num):
        ideaDcg = 1 / math.log(ast.literal_eval(doc[1]) + 1, 2)

        if num > 0:
            self.ideaDcgTable.append(self.ideaDcgTable[-1] + ideaDcg)
        else:
            self.ideaDcgTable.append(self.ideaDcgTable[-1])


        if doc[4] == 1:
            self.DcgTable.append(self.DcgTable[-1] + ideaDcg)
        else:
            self.DcgTable.append(self.DcgTable[-1])

        self.ndcgTable.append(self.DcgTable[-1] / self.ideaDcgTable[-1])

        return self.ndcgTable[-1]


    def writeP20(self):
        with open ("table.txt", 'a') as f:
            f.write("\n");
            f.write("P@20 for three queries are : \n")
            for i in self.p20:
                f.write("%r \n"%i)

    def writeMAP(self):
        with open ("table.txt", 'a') as f:
            f.write("\n");
            f.write("MAP value is \n")
            sumAvg = 0
            for i in self.avg:
                sumAvg += sum(self.avg[i]) / float(len(self.avg[i]))

            MAP = sumAvg / len(self.avg.keys())
            f.write("%r \n"%MAP)


    def writeToFile(self):
        # for each query
        #TODO 1
        for i in range(1,4):
            self.DcgTable = [0]
            self.ideaDcgTable = [0]
            self.ndcgTable = []

            relevantTotal = len(self.relevance[i])
            new_relevantTotal = relevantTotal
            relevantNum = 0
            # for each retrived document
            for j in self.output[(i - 1) * 100 : i * 100]:
                if ast.literal_eval(j[2]) in self.relevance[i]:
                    j[4] = 1
                    relevantNum += 1
                    self.avg[i].append(self.precision(j, relevantNum))
                    #  print j
                else:
                    j[4] = 0
                j[5] = self.precision(j, relevantNum)
                j[6] = self.recall(j,relevantNum,relevantTotal)
                j[7] = self.ndcg(j,new_relevantTotal)
                new_relevantTotal -= 1

                #  find P@20
                if self.output.index(j) == ((i - 1)*100 + 19):
                    self.p20.append(j[5])

        with open("table.txt",'wb') as f:
            for i in self.output:
                # queryid rank doc_id doc_score relevance precision recall ndcg
                # TODO 3
                # orginal format
                #  f.write(" ".join(str(j) for j in i))
                #  f.write('\n')

                #  trying beautiful format
                f.write('%r %3r %4r %10.5f %r %10.5f %10.5f %10.5f\n'%\
                        (ast.literal_eval(i[0]),ast.literal_eval(i[1]),ast.literal_eval(i[2]),\
                        ast.literal_eval(i[3]), i[4], i[5], i[6], i[7]))
                #  f.write("%r %r %r %r %r %r %r %r"%(i[0],  i[1],  i[2],  i[3],  i[4],  i[5],  i[6],  i[7]))
        #  #  for i in self.output:
            #  print i


        # write results to Q1_table, Q2_table, Q3_table

# run with
#  python hw5.py results.txt relevance.txt

if __name__ == '__main__':
    result , relevance = sys.argv[1], sys.argv[2]
    a = Solution(result,relevance)
    a.writeToFile()
    a.writeP20()
    a.writeMAP()


