import math
import time
from collections import OrderedDict
import sys

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
        self.M_num = {}

        for p in self.M:
            self.M_num[p] = len(self.M[p])
            for page in self.M[p]:
                if page in self.L:
                    self.L[page] += 1
                else:
                    self.L[page] = 1

        print "top 50 pages by in-link count:"
        self.sort_by_value(self.M_num)

        self.no_in_links_num = 0
        for i in self.M_num:
            if self.M_num[i] == 0:
                self.no_in_links_num += 1

        self.S = self.P - set(self.L.keys())
        self.N = len(self.P)
        self.PR = {}
        self.newPR = {}

        # init self.newPR
        for p in self.P:
            self.PR[p] = 1.0 / self.N

        print "proportion of no in-links"
        print "%r / %r"%(self.no_in_links_num , self.N)
        print "proportion of no out-links"
        print "%r / %r"%(len(self.S) , self.N)


    def page_rank(self):
        print self.cal_per(self.PR)
        # remember iteration times

        for i in range(1,101):
            sinkPR = 0
            for p in self.S:
                sinkPR += self.PR[p]
            for p in self.P:
                self.newPR[p] = (1.0 - self.d) / self.N
                self.newPR[p] += self.d * 1.0 * sinkPR / self.N
                for q in self.M[p]:
                    self.newPR[p] += self.d * 1.0 * self.PR[q] / self.L[q]

            for p in self.P:
                self.PR[p] = self.newPR[p]

            #  print perplexity values for each iteration
            print self.cal_per(self.PR)

            if i in [1, 10, 100]:
                print "%d iteration value" %(i)
                for i in self.PR.items():
                    print i

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
    file = sys.argv[1]

    a = Solution(file)
    page_rank_value = a.page_rank()
    a.sort_by_value(page_rank_value)

    less_than_init_num = 0
    # find values less than initial value
    for i in page_rank_value:
        if page_rank_value[i] < (1.0 / 183811):
            less_than_init_num += 1

    print "proportion less than initial value"
    print "%r / %r" %(less_than_init_num, 183811)

    print "top 50 pages by pagerank"

    end_time = time.time()
    print "total running time: %d" %(end_time - start_time)



