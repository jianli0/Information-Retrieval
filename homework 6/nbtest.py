import sys
import os
import ast
import math
from collections import OrderedDict

class Solution:
    # read parameters for postive and negative models
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
        self.result = {}

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

        # start test and write results to outputFile
    def test(self):
        for file in os.listdir(os.getcwd() + self.directory):
            self.result[file] = self.testForSingleFile(os.getcwd() + self.directory + '/' + file)

        with open(self.predictFile, 'wb') as f:
            for i in self.result:
                f.write("%8r %8r %10.5f %10.5f\n"%(i,self.result[i][0],self.result[i][1],self.result[i][2]))

        self.result = {}

    # test for a single File
    # return 1 : pos, 0 : neg
    def testForSingleFile(self,file):
        # token file and
        negScore = self.testForNeg(file)
        posScore = self.testForPos(file)
        print posScore
        print negScore
        if posScore > negScore:
            return ["pos",posScore,negScore]
        else:
            return ["neg",posScore,negScore]

    def testForPos(self,file):
        score = 0
        with open(file) as f:
            lines = f.read().split("\n")
            for line in lines:
                for j in line.split():
                    if j in self.posModel.keys():
                        score += math.log((self.posModel[j] + 1) * 1.0 / (self.posTotal + self.posV),2)
            return score * self.Ppos

    def testForNeg(self,file):
        score = 0
        score *= self.Pneg
        with open(file) as f:
            lines = f.read().split("\n")
            for line in lines:
                for j in line.split():
                    if j in self.negModel.keys():
                        score += math.log((self.negModel[j] + 1) * 1.0 / (self.negTotal + self.negV),2)
            return score * self.Pneg

    # top 20 terms
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
    a.test()
    #  a.top20Term()

