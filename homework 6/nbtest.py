class Solution:
    def __init__(self):
        pass

    def readDocs(self):
        pass

    def printModel(self)



#  run with
#  TODO 1
#  python nbtest.py modelfile /textcat/test/ predictions.txt

if __name__ == '__main__':
    model , directory = sys.argv[1], sys.argv[2]
    a = Solution(model)
    a.printModel()


