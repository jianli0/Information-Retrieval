import sys
import math
import time
import ast

class Solution:
    def __init__(self , file1 , file2, num):
        self.indexFile = file1
        self.queryFile = file2
        self.maxNum = num
        #  todo
        #  dl
        #  avdl
        #  K
        self.N = 3204
        #  self.K = 1.2 * (0.25 + 0.75 * dl / avdl)

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

        print self.index
        print self.query

    def

    def bm25(self):
        pass
        #  deal with each query
        for query in self.query:
            #  deal with each term
            for term in query:
                if term in self.index.keys():
                    ni = len(self.index[term])
                    for i in range(1 , self.N + 1):
                        if

                else:
                    fi = 0
                    ni = 0

                score += self.calScore(len() , )

    def testForkeys(self):
        pass


    def calScore(self, ni, fi):
        pass
        res = (self.N - ni + 0.5) / (ni + 0.5) * \
                2.2 * fi / (self.K + fi) * \
                101 * fi / (100 + fi)
        return log(res ,2)



if __name__ == '__main__':
    start_time =  time.time()

    inFile , outFile , maxNum = sys.argv[1] , sys.argv[2], sys.argv[3]
    a = Solution(inFile , outFile, maxNum)
    end_time = time.time()
    print "total running time: %d" %(end_time - start_time)

#  run with
#  python bm25.py index.txt queries.txt 100
