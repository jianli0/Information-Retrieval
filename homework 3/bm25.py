import sys
import math

class Solution:
    def __init__(self , file1 , file2, num):
        self.inFile = file1
        self.outFile = file2
        self.maxNum = num

    def bm25(self):
        pass

    def calScore(self):
        res =


        return log( ,2)

    def calK(self):

        pass


if __name__ == '__main__':
    start_time =  time.time()

    inFile , outFile , maxNum = sys.argv[1] , sys.argv[2], sys.argv[3]
    a = Solution(inFile , outFile, maxNum)
    a.writeToFile()
    end_time = time.time()
    print "total running time: %d" %(end_time - start_time)

#  run with
#  python bm25.py index.txt queries.txt 100
