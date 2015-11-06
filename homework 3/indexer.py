import sys
import time

__author__ ='jian li'

class Solution:
    def __init__(self,file1,file2,file3):
        self.inFile = file1
        self.outFile = file2
        self.tokenFile = file3

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


    #inverted index
    def index(self):
        tf = {}
        doc = self.token()

        #  print doc
        #  print len(doc)

        for i in range(len(doc)):
            for j in doc[i]:
                if j in tf.keys():
                    tf[j].add((i + 1 , doc[i].count(j)))
                else:
                    tf[j] = set()
                    tf[j].add((i + 1 , doc[i].count(j)))
        return tf

    def writeTokenToFile(self,tokendoc):
        with open (self.tokenFile,'wb') as f:
            for i in tokendoc:
                f.write("%r\n"%i)


    def writeIndexToFile(self):
        tf = self.index()
        with open (self.outFile ,'wb') as f:
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

    inFile , outFile, tokenFile = sys.argv[1] , sys.argv[2], sys.argv[3]
    a = Solution(inFile , outFile, tokenFile)
    #  a.writeIndexToFile()
    a.token()

    end_time = time.time()
    print "total running time: %d" %(end_time - start_time)

#  run with
#  python tccorpus.txt index.txt token.txt
