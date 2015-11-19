import sys
import ast
from collections import OrderedDict
import matplotlib.pyplot as plt
#  run with
#  python sortedFreqList.py termFrequency.txt sortedFreqList.txt


def sortFreq(file1,file2):
    with open(file1) as f:
        fread = f.read()
        lines = fread.split()
    dic = {}

    for i in range(0,len(lines) - 1,2):
        dic[lines[i]] = ast.literal_eval(lines[i + 1])

    sortedDict = OrderedDict(sorted(dic.items(), key=lambda x: x[1] , reverse = True))


    #  with open(file2,'wb') as f:
        #  for i in sortedDict:
            #  f.write("%r %d\n"%(i,sortedDict[i]))

    return sortedDict

def zipf(OrderedDic):
    totalFreq = sum(OrderedDic[i] for i in OrderedDic)
    prob = []
    rank = []
    rankNum = 1
    for i in OrderedDic:
        prob.append(OrderedDic[i] * 1.0 / totalFreq)
        rank.append(rankNum)
        rankNum += 1

    plt.scatter(rank, prob, c = 'r')
    plt.ylabel('probability')
    plt.xlabel('rank')
    plt.show()

if __name__ == '__main__':
    file1, file2 = sys.argv[1],sys.argv[2]
    sortedFreqList = sortFreq(file1, file2)
    zipf(sortedFreqList)
