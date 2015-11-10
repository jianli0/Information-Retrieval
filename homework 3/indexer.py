import sys
import time

__author__ ='jian li'

class Solution:
    def __init__(self,file1,file2):
        self.inFile = file1
        self.outFile = file2

    # tokenization
    def token(self):
        tokendoc = [[]]
        with open(self.inFile) as f:
            fread = f.read()
            lines = fread.split("\n")
            content = fread.split()

        i = 2
        while i < len(content):
            if content[i] == '#':
                tokendoc.append([])
            elif not self.isNum(content[i]):
                tokendoc[-1].append(content[i])
            i += 1

        self.writeTokenToFile(tokendoc)
        return tokendoc

    #inverted index
    def index(self):
        tf = {}
        doc = self.token()

        for i in range(len(doc)):
            for j in doc[i]:
                if j in tf.keys():
                    tf[j].add((i + 1 , doc[i].count(j)))
                else:
                    tf[j] = set()
                    tf[j].add((i + 1 , doc[i].count(j)))
        self.writeIndexToFile(tf)

    #  write token to file
    def writeTokenToFile(self,tokendoc):
        with open (self.outFile,'wb') as f:
            f.write("%d\n"%len(tokendoc))
            avdl = sum(len(i) for i in tokendoc) * 1.0 / len(tokendoc)
            f.write("%f\n"%avdl)
            for i in range(len(tokendoc)):
                f.write("%d\n"%(i + 1))
                f.write("%d\n"%(len(tokendoc[i])))
            f.write("-"*50)
            f.write("\n")

    #  write inverted index to file
    def writeIndexToFile(self,tf):
        with open (self.outFile ,'ab') as f:
            for i in tf.keys():
                f.write("%r\n"%i)
                f.write("%r\n"%(list(tf[i])))

    # return True if the string is all number
    def isNum(self,string):
        nums = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
        res = True
        for i in string:
            res = res and (i in nums)
        return res


if __name__ == '__main__':
    start_time =  time.time()

    inFile , outFile = sys.argv[1] , sys.argv[2]
    a = Solution(inFile , outFile)
    a.token()
    a.index()

    end_time = time.time()
    print "total running time: %d" %(end_time - start_time)

#  run with
#  python indexer.py tccorpus.txt index.txt
