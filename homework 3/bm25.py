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

        # read the inverted index
        with open(self.indexFile) as f:
            fRead = f.read()
            lines = fRead.split("\n")

        #  print '-'*50
        #  for i in range(len(lines)):
            #  if ast.literal_eval(lines[0]) == 'portabl':
                #  break
        #  print i
        #  print type(lines)
        #  print ast.literal_eval(lines[0]) == 'orthogon'

        #  print lines.index('orthogon')
        #  print lines.index('clutter')
        #  print lines.index('portabl')

        self.index = {}
        for i in range(0,len(lines) - 1,2):
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


    def calK(self, dl):
         return  1.2 * (0.25 + 0.75 * dl / self.avdl)

    def bm25(self):
        #  deal with each query
        for q in range(len(self.query)):
            #  score for each doc for a query
            for i in range(len(self.token)):
                score = 0
                dl = len(self.token[i])
                K = self.calK(dl)
                for term in self.query[q]:
                    #  print term
                    #  if term in self.index.keys():
                    ni = len(self.index[term])
                    fi = self.token[i].count(term)
                    #  else:
                        #  ni = 0
                        #  fi = 0
                    score += self.calScore(ni,fi,K )
                self.scores[(q+1,i+1)] = score

        print score

    def calScore(self, ni, fi, K):
        print ni,fi,K,self.N
        res = 1.0 * (self.N - ni + 0.5) / (ni + 0.5) * \
                2.2 * fi / 1.0 * (K + fi) * \
                101 * fi / 1.0 * (100 + fi)
        # debug
        if res == 0:
            return 0
        else:
            return math.log(res ,2)

if __name__ == '__main__':
    start_time =  time.time()
    inFile , outFile , tokenFile, maxNum = sys.argv[1] , sys.argv[2], sys.argv[3],sys.argv[4]
    a = Solution(inFile , outFile, tokenFile ,maxNum)
    a.bm25()
    end_time = time.time()
    print "total running time: %d" %(end_time - start_time)

#  run with
#  python bm25.py index.txt queries.txt token.txt 100
