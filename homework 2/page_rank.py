# problems
# 1 how to deal with converge
# 2 how to find sink nodes
# 3 how to get L(q)

import math
class Solution:
    def __init__(self):
        file = "/Users/lijian/Dropbox/Courses/15Fall-Information Retrieval/homework 2/wt2g_inlinks.txt"
        file1 = "/Users/lijian/Dropbox/Courses/15Fall-Information Retrieval/homework 2/example.txt"

        lines = [line.rstrip('\n').split() for line in open(file1)]

        self.L = {}
        self.M = {}
        self.P = set()

        # traverse the lines
        # get P,L (all pages, out-links)
        for i in range(len(lines)):
            self.M[lines[i][0]] = []
            self.P.append(lines[i][0])
            for j in range(1, len(lines[i])):
                # solve M
                self.M[lines[i][0]].append(lines[i][j])
                # solve P
                self.P.append(lines[i][j])
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


    def page_rank(self,convergeTime):
        # if self.Per(self.PR)
        while #not converge:
            sinkPR = 0
        for p in S:
            sinkPR += self.PR[p]
        for p in P:
            self.newPR[p] = (1.0 - d) / N
            self.newPR[p] += d * 1.0 * sinkPR / N
            for q in self.M[p]:
                self.newPR[p] += d * 1.0 * self.PR[q] / len(self.L[q])
        for p in P:
            self.PR[p] = self.newPR(p)

        # perplexity values
        print self.PR

        return self.PR

    # calculate perplextiy for PR
    def calPer(self, PR):
        H = 0
        for i in PR:
            H += i * math.log(i,2)
        return 2**(-H)




if __name__ == '__main__':
    a = Solution()
    print a.page_rank()




