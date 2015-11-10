import sys
import math
import time
import ast
import operator

__author__ ='jian li'

#  run with
#  python bm25.py index.txt queries.txt 100

class Solution:
    def __init__(self , file1 , file2 , num):
        self.scores = {}
        self.indexFile = file1
        self.queryFile = file2
        self.resultsFile = "results.txt"
        self.maxNum = num

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

        #  print self.index['emeri'][0]
        #  print self.index['emeri'][0][0]
        #  print self.index['emeri'][0][1]

        #  read the query
        with open(self.queryFile) as f:
            fRead = f.read()
            lines = fRead.split("\n")
        self.query = [line.split() for line in lines if len(line) > 0]

        #  debug
        #  print self.index
        #  print self.avdl
        #  print self.docLength
        #  print self.N
        #  print '-'*50
        #  for i in range(len(indexFile)):
            #  if ast.literal_eval(indexFile[i]) == 'portabl':
                #  print "find it"
                #  break
        #  print i
        #  print ast.literal_eval(indexFile[0]) == 'orthogon'


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
                        for j in self.index[term]:
                            if (i + 1) == j[0]:
                                fi = j[1]
                                break
                    else:
                        ni = 0
                        fi = 0
                    score += self.calScore(ni,fi,K)

                eachQueryScores[(q+1,i+1)] = score
            #  debug
            #  for i in eachQueryScores.items():
                #  print i

            sorted_x = sorted(eachQueryScores.items(), key = operator.itemgetter(1), reverse = True)
            #  debug
            #  for x in sorted_x[0:100]:
                #  print x
            #  self.writeEachQueryScores(sorted_x[0:100])

    #  write top maxNum of scores to results
    def writeEachQueryScores(self, lis):
        with open (self.resultsFile,'ab') as f:
            for i in range(len(lis)):
                f.write("%-3r %-3r %-5r %-4r %-10.3f %-10r\n"\
                        %(lis[i][0][0],"Q0",lis[i][0][1],i + 1,lis[i][1],"bm25"))

    def calScore(self, ni, fi, K):
        #  print ni,fi,K,self.N
        t1 = math.log((self.N - ni + 0.5) / (ni + 0.5))
        t2 = 2.2 * fi / 1.0 * (K + fi) * \
        t3 = 101 * fi / 1.0 * (100 + fi)
        print "%r %r %r \n"%(t1,t2,t3)
        return t1*t2*t3

    def calK(self, dl):
        #  print "dl is %d\n"%dl
        return  1.2 * (0.25 + 0.75 * dl / self.avdl)

if __name__ == '__main__':
    start_time =  time.time()
    inFile , outFile , maxNum = sys.argv[1] , sys.argv[2], sys.argv[3]
    a = Solution(inFile , outFile, maxNum)
    a.bm25()
    end_time = time.time()
    print "total running time: %d" %(end_time - start_time)

