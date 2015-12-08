import sys
import os
import ast

class Solution:
    def __init__(self,modelfile,directory):
        self.model = modelfile
        self.directory = directory

        self.Ppos = 0
        self.Pneg = 0
        self.posModel = {}
        self.posTotal = 0
        self.negModel = {}
        self.negTotal = 0

        with open('pos'+self.model) as f:
            lines = f.read().split('\n')
            print lines[0]
            self.Ppos = ast.literal_eval(lines[0])
            for i in range(1,len(lines),2):
                self.posModel[lines[i]] = ast.literal_eval(lines[i + 1])
                self.posTotal += ast.literal_eval(lines[i + 1])

        with open('neg'+self.model) as f:
            lines = f.read().split('\n')
            self.Pneg = ast.literal_eval(lines[0])
            for i in range(1,len(lines),2):
                self.negModel[lines[i]] = ast.literal_eval(lines[i + 1])
                self.negTotal += ast.literal_eval(lines[i + 1])

        print self.posModel
        print self.posTotal
        #  print self.posModel





#  run with
#  TODO 1
#  python nbtest.py modelfile /textcat/test/ predictions.txt


if __name__ == '__main__':
    modelfile , directory = sys.argv[1], sys.argv[2]
    a = Solution(modelfile, directory)

