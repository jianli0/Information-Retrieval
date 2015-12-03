import sys
import ast

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
        self.DcgTable = []
        self.ideaDcgTable = []
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

        #  print self.relevance
        #  {1: [1523, 2080, 2246, 2629, 3127]}
        # reading output from hw3 and relevance document

    def precision(self, doc, isRelevance, relevantNum):
        if isRelevance:
            return (relevantNum + 1)* 1.0 / doc[1]
        else:
            return relevantNum * 1.0 / doc[1]

    def recall(self, doc, isRelevance, relevantNum, relevantTotal):
        if isRelevance:
            return (relevantNum + 1)* 1.0 / relevantTotal
        else:
            return relevantNum * 1.0 / relevantTotal

    def ndcg(self, doc, isRelevance):
        if isRelevance:
            dcg =
            self.ideaDcgTable.append(self.ideaNdcgTable[-1] + dcg)
            self.ndcgTable.append()

        return self.ndcgTable[-1]


    def p20(self,):
        pass

    def writeToFile(self):
        # for each query
        for i in range(1,4):
            # for each retrived document
            for j in self.output:
                if self.output[j][1] in self.relevance[i]:
                    self.output[i][3] = 1
                else:
                    self.output[i][3] = 0
                self.output[i][4] = self.precision()
                self.output[i][5] = self.precision()
                self.output[i][6] = self.precision()
        # write results to Q1_table, Q2_table, Q3_table

# run with
#  python hw4.py results.txt relevance.txt

if __name__ == '__main__':
    result , relevance = sys.argv[1], sys.argv[2]
    a = Solution(result,relevance)


