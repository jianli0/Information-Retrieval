import sys
import os
import ast
import math
from collections import OrderedDict

class Solution:
    def __init__(self,modelfile,directory, predictFile):
        self.model = modelfile
        self.directory = directory
        self.predictFile = predictFile

        self.Ppos = 0
        self.Pneg = 0
        self.posModel = {}
        self.posTotal = 0
        self.negModel = {}
        self.negTotal = 0
        self.resultMap = {1 : "pos", 0 : "neg"}

        self.top20Pos = {}
        self.top20Neg = {}

        with open('pos'+self.model) as f:
            lines = f.read().split('\n')
            self.Ppos = ast.literal_eval(lines[0])

            for i in range(1,len(lines) - 1,2):
                self.posModel[lines[i]] = ast.literal_eval(lines[i + 1])
                self.posTotal += ast.literal_eval(lines[i + 1])
            self.posV = len(self.posModel.keys())

        with open('neg'+self.model) as f:
            lines = f.read().split('\n')
            self.Pneg = ast.literal_eval(lines[0])

            for i in range(1,len(lines) - 1,2):
                self.negModel[lines[i]] = ast.literal_eval(lines[i + 1])
                self.negTotal += ast.literal_eval(lines[i + 1])

            self.negV = len(self.negModel.keys())

        #  print self.posModel
        #  print self.posTotal
        #  print self.posModel

        # start test and write results to outputFile
    def test(self,directory,outputFile):
        return 0

    # test for a single File
    # return 1 : pos, 0 : neg
    def testForSingleFile(self,file):
        # token file and
        return 0

    def top20Term(self):
        common = list(set(self.posModel.keys()) & set(self.negModel.keys()))
        for i in common:
            self.top20Pos[i] = math.log((self.posModel[i] * 1.0) / self.posTotal,2)\
            / math.log((self.negModel[i] * 1.0) / self.negTotal,2)

            self.top20Neg[i] = math.log((self.negModel[i] * 1.0) / self.negTotal,2)\
            / math.log((self.posModel[i] * 1.0) / self.posTotal,2)

        sortedtop20Pos = OrderedDict(sorted(self.top20Pos.items(), key = lambda x:x[1], reverse = True))
        sortedtop20Neg = OrderedDict(sorted(self.top20Neg.items(), key = lambda x:x[1], reverse = True))

        with open("top20pos.txt",'wb') as f:
            for i in range(20):
                f.write("%r %r\n"%(sortedtop20Pos.items()[i][0], sortedtop20Pos.items()[i][1]))

        with open("top20neg.txt",'wb') as f:
            for i in range(20):
                f.write("%r %r\n"%(sortedtop20Neg.items()[i][0], sortedtop20Neg.items()[i][1]))
#  run with
#  TODO 1
#  python nbtest.py model.txt /textcat/test/ predictions.txt

if __name__ == '__main__':
    modelfile ,testDir ,predFile = sys.argv[1], sys.argv[2] , sys.argv[3]
    a = Solution(modelfile, testDir,predFile)
    #  a.top20Term()

