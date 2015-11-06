import sys
import math
import time
import ast

class Solution:
    def __init__(self , file1 , file2, file3, num):
        self.scores = {}
        self.indexFile = file1
        self.queryFile = file2
        self.tokenFile = file3
        self.maxNum = num
        #  todo
        #  avdl

        # read the inverted index
        with open(self.indexFile) as f:
            fRead = f.read()
            lines = fRead.split("\n")
        self.index = {}
        for i in range(0,3203,2):
            self.index[ast.literal_eval(lines[i])] = ast.literal_eval(lines[i + 1])

        # read the query
        with open(self.queryFile) as f:
            fRead = f.read()
            lines = fRead.split("\n")

        self.query = [line.split() for line in lines if len(line) > 0]

        # read the token file
        with open(self.tokenFile) as f:
            fRead = f.read()
            lines = fRead.split("\n")
        self.token = [ast.literal_eval(line) for line in lines if len(line) > 0]


        self.N = len(self.token)
        self.avdl = sum(len(i) for i in self.token) * 1.0 / self.N

        #  debug
        #  print self.index
        #  print self.query
        #  print len(self.token)
        #  print self.token[0]
        #  print type(self.token[0])
        #  print self.token[-1]
        #  print self.token[1]


    def calK(self, dl):
         return = 1.2 * (0.25 + 0.75 * dl / self.avdl)

    def bm25(self):
        #  deal with each query
        for query in self.query:
            #  score for each doc for a query
            for i in range(len(self.token)):
                score = 0
                dl = len(self.token[i])
                for term in query:
                    ni = len(self.index[term])
                    fi = self.token[i].count(term)

                    score += self.calScore(len() , )

    def calScore(self, ni, fi, K):
        res = (self.N - ni + 0.5) / (ni + 0.5) * \
                2.2 * fi / (K + fi) * \
                101 * fi / (100 + fi)
        return log(res ,2)

if __name__ == '__main__':
    start_time =  time.time()

    inFile , outFile , tokenFile, maxNum = sys.argv[1] , sys.argv[2], sys.argv[3],sys.argv[4]
    a = Solution(inFile , outFile, tokenFile ,maxNum)
    end_time = time.time()
    print "total running time: %d" %(end_time - start_time)

#  run with
#  python bm25.py index.txt queries.txt token.txt 100
