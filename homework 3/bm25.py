import sys
import math
import time
import ast
import operator

__author__ ='jian li'

#  run with
#  python bm25.py index.txt queries.txt 100 > results.eval
#  python bm25.py index.txt Q1.txt 3204 > results1.results1.eval
#  python bm25.py index.txt Q2.txt 3204 > results2.eval

class Solution:
    def __init__(self , file1 , file2 , num):
        self.scores = {}
        self.indexFile = file1
        self.queryFile = file2
        self.maxNum = int(num)

        # read the inverted index
        with open(self.indexFile) as f:
            fRead = f.read()
            lines = fRead.split("\n")

        self.N = ast.literal_eval(lines[0])
        self.avdl= ast.literal_eval(lines[1])

        indexFile = lines[2*self.N + 3:]
        length = lines[2 : 2*self.N + 2]

        #  read the doc length
        self.docLength = []
        for i in range(0,len(length) - 1, 2):
            self.docLength.append(ast.literal_eval(length[i + 1]))

        #  read inverted index
        self.index = {}
        for i in range(0,len(indexFile) - 1,2):
            self.index[ast.literal_eval(indexFile[i])] = ast.literal_eval(indexFile[i + 1])

        #  read the query
        with open(self.queryFile) as f:
            fRead = f.read()
            lines = fRead.split("\n")
        self.query = [line.split() for line in lines if len(line) > 0]


    def bm25(self):
        #  deal with each query
        for q in range(len(self.query)):
            #  score for each doc for a query
            eachQueryScores = {}
            for i in range(len(self.docLength)):
                score = 0
                dl = self.docLength[i]
                K = self.calK(dl)
                for term in self.query[q]:
                    if term in self.index.keys():
                        ni = len(self.index[term])
                        fi = 0
                        if (i + 1) in self.index[term]:
                            fi = self.index[term][i + 1]
                    else:
                        ni = 0
                        fi = 0
                    score += self.calScore(ni,fi,K)
                if score > 0:
                    eachQueryScores[(q+1,i+1)] = score
            print len(eachQueryScores)

            #  print top 100
            #  sorted_x = sorted(eachQueryScores.items(), key = operator.itemgetter(1), reverse = True)
            #  for i in range(self.maxNum):
                #  print "%-5r %r %-5r %-3r %-10f %r"\
                        #  %(sorted_x[i][0][0],"Q0",sorted_x[i][0][1],i + 1,sorted_x[i][1],"jianli")

    def calScore(self, ni, fi, K):
        t1 = math.log((self.N - ni + 0.5) / (ni + 0.5))
        t2 = 2.2 * fi / (K + fi)
        #  t3 = 101 * 1 / 1.0 * (100 + 1)
        return t1*t2

    def calK(self, dl):
        return  1.2 * (0.25 + 0.75 * dl / self.avdl)

if __name__ == '__main__':
    start_time =  time.time()
    inFile , outFile , maxNum = sys.argv[1] , sys.argv[2], sys.argv[3]
    a = Solution(inFile , outFile, maxNum)
    a.bm25()
    end_time = time.time()
    #  print "total running time: %d" %(end_time - start_time)

