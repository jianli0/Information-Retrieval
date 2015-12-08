import sys
import os

class Solution:
    def __init__(self, dire, modelfile):
        self.model = modelfile
        self.directory = dire

        self.posDir = self.directory + 'pos'
        self.negDir = self.directory + 'neg'

        #TODO 2
        self.posNum = 0
        self.negNum = 0

        self.Ppos = 0
        self.Pneg = 0

        self.posModel = {}
        self.negModel = {}

    def readDocs(self):
        self.posNum = len(os.listdir(self.posDir))
        self.negNum = len(os.listdir(self.negDir))

        self.Ppos = self.posNum * 1.0 / (self.posNum + self.negNum)
        self.Pneg = self.negNum * 1.0 / (self.posNum + self.negNum)
        print"self.pos is %f"%self.Ppos
        print"self.pos is %f"%self.Ppos

        for file in os.listdir(self.posDir):
            self.token(self.posDir + '/' + file,self.posModel)

        for file in os.listdir(self.negDir):
            self.token(self.negDir +'/' + file,self.negModel)

    def token(self, file, model):
        # TODO now
        with open(file) as f:
            lines = f.read().split("\n")
            for line in lines:
                for j in line.split():
                    if j in model:
                        model[j] += 1
                    else:
                        model[j] = 1

    def ignoreLessThan5(self):
        common = list(set(self.posModel.keys()) & set(self.negModel.keys()))
        posLeft = list(set(self.posModel.keys()) - set(common))
        negLeft = list(set(self.negModel.keys()) - set(common))

        for i in common:
            if (self.posModel[i] + self.negModel[i]) < 5:
                del self.posModel[i]
                del self.negModel[i]

        for i in posLeft:
            if self.posModel[i] < 5:
                del self.posModel[i]

        for i in negLeft:
            if self.negModel[i] < 5:
                del self.negModel[i]

    def writeModel(self):
        self.ignoreLessThan5()
        with open('pos'+ self.model,'wb') as f:
            for i in self.posModel:
                f.write(i)
                f.write('\n')
                f.write('%r\n'%self.posModel[i])

        with open('neg'+ self.model,'wb') as f:
            for j in self.negModel:
                f.write(j)
                f.write('\n')
                f.write('%r\n'%self.negModel[j])

#  run with
#  TODO 1
#  python nbtrain.py /textcat/train/ model.txt

if __name__ == '__main__':
    directory , modelfile = sys.argv[1], sys.argv[2]
    a = Solution(os.getcwd() + directory, modelfile)
    #  a.writeModel()
    #  print directory,modelfile
    # loading the module
    a.readDocs()
    a.writeModel()



