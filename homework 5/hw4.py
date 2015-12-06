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
        print self.relevance
        #  {1: [1523, 2080, 2246, 2629, 3127]}

    def precision(self, doc, relevantNum):
        if doc[4] == 1:
            return (relevantNum + 1)* 1.0 / ast.literal_eval(doc[1])
        else:
            return relevantNum * 1.0 / ast.literal_eval(doc[1])

    def recall(self, doc, relevantNum, relevantTotal):
        if doc[4] == 1:
            return (relevantNum + 1)* 1.0 / relevantTotal
        else:
            return relevantNum * 1.0 / relevantTotal

    def ndcg(self, doc):
        ideaDcg = 1 / math.log(ast.literal_eval(doc[1]) + 1, 2)
        self.ideaDcgTable.append(self.ideaDcgTable[-1] + ideaDcg)

        if doc[4] == 1:
            self.DcgTable.append(self.DcgTable[-1] + ideaDcg)
        else:
            self.DcgTable.append(self.DcgTable[-1])

        self.ndcgTable.append(self.DcgTable[-1] / self.ideaDcgTable[-1])

        return self.ndcgTable[-1]


    def p20(self):
        pass

    def writeToFile(self):
        # for each query

        #TODO 1
        for i in range(1,4):
            relevantTotal = len(self.relevance[i])
            relevantNum = 0
            # for each retrived document
            for j in self.output[(i - 1) * 100 : i * 100]:
                #  print "j[2] is %r, relevance[i] is %r"%(ast.literal_eval(j[2]), self.relevance[i])
                #  print  ast.literal_eval(j[2]) in self.relevance[i]
                if ast.literal_eval(j[2]) in self.relevance[i]:
                    j[4] = 1
                    relevantNum += 1
                    print j
                else:
                    j[4] = 0
                j[5] = self.precision(j, relevantNum)
                j[6] = self.recall(j,relevantNum,relevantTotal)
                j[7] = self.ndcg(j)

        with open("table.txt",'wb') as f:
            for i in self.output:
                # queryid rank doc_id doc_score relevance precision recall ndcg
                f.write(" ".join(str(j) for j in i))
                f.write('\n')
                # TODO 3
                #  f.write('%r %3r %4r %10.6f %r %10.6f %10.6f %10.6f\n'%\
                        #  i[0], i[1], i[2], ast.literal_eval(i[3]), i[4], ast.literal_eval(i[5]),\
                        #  ast.literal_eval(i[6]), ast.literal_eval(i[7]))
        #  #  for i in self.output:
            #  print i


        # write results to Q1_table, Q2_table, Q3_table

# run with
#  python hw4.py results.txt relevance.txt

if __name__ == '__main__':
    result , relevance = sys.argv[1], sys.argv[2]
    a = Solution(result,relevance)
    a.writeToFile()


