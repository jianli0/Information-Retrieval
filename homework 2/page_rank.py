# problems
# 1 how to deal with converge
# 2 how to find sink nodes
# 3 how to get L(q)

class Solution:

    def __init__(self, in_links, d):
        self.P =
        self.S =
        self.M = inlinks

        self.L = [] # remains to be done
        self.N = len(self.P)

        self.PR = []
        self.newPR = []

        for p in P:
            PR.append(1.0 / N)
            # init self.newPR



    def page_rank(self,):
        while # not converge:
            self.sinkPR = 0
        for p in S:
            self.sinkPR += self.PR[p]
        for p in P:
            self.newPR[p] = (1.0 - d) / N
            self.newPR[p] += d * self.sinkPR / N
            for q in self.M:
                self.newPR[p] += d * self.PR[q] / self.L[q]
        for p in P:
            self.PR[p] = self.newPR(p)

        return PR




