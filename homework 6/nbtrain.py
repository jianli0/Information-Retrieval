import sys
import imp

class Solution:
    def __init__(self,modelfile):
        self.model = modelfile
        self.posDir = 0
        self.negDir = 0
        #TODO 2
        self.Ppos = 0
        self.Pneg = 0

        self.posModel = {1:1,2:2}
        self.negModel = {1:2,2:1}

    def readDocs(self):

        pass

    def writeModel(self):
        self.model
        #  with open(self.model,'wb') as f:
            #  for i in self.posModel.items():
                #  f.write("%r\n"%i)
            #  for j in self.negModel.items():
                #  f.write()




#  run with
#  TODO 1
#  python nbtrain.py /textcat/train/  modelfile
#  python nbtrain.py /textcat/train/ model

if __name__ == '__main__':
    directory , modelfile = sys.argv[1], sys.argv[2]
    # load the module
    fp, pathname, description = imp.find_module(modelfile)
    loadedModel =  imp.load_module(modelfile, fp, pathname, description)
    print loadedModel.posModel



