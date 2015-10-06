# problems
# 1 how to deal with converge
# 2 how to find sink nodes
# 3 how to get L(q)

import math
import time
class Solution:
    def __init__(self):
        file = "/Users/lijian/Dropbox/Courses/15Fall-Information Retrieval/homework 2/wt2g_inlinks.txt"

        # test on file1
        file1 = "/Users/lijian/Dropbox/Courses/15Fall-Information Retrieval/homework 2/example.txt"

        # lines = [line.rstrip('\n').split() for line in open(file1)]

        f = open(file1)
        lines = []
        for line in f:
            lines.append(line.split())

        self.L = {}
        self.M = {}
        self.P = set()
        self.d = 0.85

        # traverse the lines
        # get P,L (all pages, out-links)
        for i in range(len(lines)):
            self.M[lines[i][0]] = []
            self.P.add(lines[i][0])
            for j in range(1, len(lines[i])):
                # solve M
                self.M[lines[i][0]].append(lines[i][j])
                # solve P
                self.P.add(lines[i][j])
                # solve L
                if lines[i][j] in self.L.keys():
                    self.L[lines[i][j]].append(lines[i][0])
                else:
                    self.L[lines[i][j]]= [lines[i][0]]

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
                    self.newPR[p] += self.d * 1.0 * self.PR[q] / len(self.L[q])

            # calculate converge times
            if (self.calPer(self.newPR) - self.calPer(self.PR)) < 1:
                self.convergeTime += 1
            else:
                self.convergeTime = 0

            for p in self.P:
                self.PR[p] = self.newPR[p]

            # print perplexity values for each iteration
            print self.PR

        return self.PR

    # calculate perplextiy for PR
    def calPer(self, PR):
        H = 0.0
        # for test
        # print PR
        for p in PR:
            H += PR[p] * math.log(PR[p],2)
        return 2**(-H)




if __name__ == '__main__':
    start_time =  time.time()
    a = Solution()
    print a.page_rank()
    end_time = time.time()
    print "total running time: %d" %(end_time - start_time)



