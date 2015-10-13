import math
import time
from collections import OrderedDict

class Solution:
    def __init__(self,filename):
        self.file = filename

        self.L = {}
        self.M = {}
        self.P = set()
        self.d = 0.85

        with open(self.file) as f:
            fread = f.read()
            lines = fread.split("\n")
            self.P = set(fread.split())

        lines = [line.split() for line in lines if len(line) > 0]

        self.M = dict((line[0],list(set(line[1:]))) for line in lines)

        for p in self.M:
            for page in self.M[p]:
                if page in self.L:
                    self.L[page] += 1
                else:
                    self.L[page] = 1

        print "top 50 pages by in-link count:"
        self.sort_by_value(self.L)

        self.S = self.P - set(self.L.keys())
        self.N = len(self.P)
        self.PR = {}
        self.newPR = {}

        # init self.newPR
        for p in self.P:
            self.PR[p] = 1.0 / self.N
        # init covergeTime
        self.convergeTime = 0


    def page_rank(self):
        while self.convergeTime <= 4:
            sinkPR = 0
            for p in self.S:
                sinkPR += self.PR[p]
            for p in self.P:
                self.newPR[p] = (1.0 - self.d) / self.N
                self.newPR[p] += self.d * 1.0 * sinkPR / self.N
                for q in self.M[p]:
                    self.newPR[p] += self.d * 1.0 * self.PR[q] / self.L[q]

            # calculate converge times
            if abs(self.cal_per(self.newPR) - self.cal_per(self.PR)) < 1:
                self.convergeTime += 1
            else:
                self.convergeTime = 0

            for p in self.P:
                self.PR[p] = self.newPR[p]

            #  print perplexity values for each iteration
            print self.cal_per(self.PR)

        return self.PR

    # calculate perplextiy for PR
    def cal_per(self, PR):
        H = 0.0
        for p in PR:
            H += PR[p] * math.log(PR[p],2)
        return 2**(-H)

    def sort_by_value(self,dic):
        sorted_by_inlink = OrderedDict(sorted(dic.items(), key = lambda t : t[1], reverse = True))
        for i in sorted_by_inlink.items()[0:50]:
            print i





if __name__ == '__main__':
    start_time =  time.time()

    # only input: file in in-link format
    file = "wt2g_inlinks.txt"
    file1 = "example.txt"

    a = Solution(file)
    a.sort_by_value(a.page_rank())
    print "top 50 pages by pagerank"

    end_time = time.time()

    print "total running time: %d" %(end_time - start_time)



