class Solution:
    def __init__(self):
        file = "/Users/lijian/Dropbox/Courses/15Fall-Information Retrieval/homework 2/wt2g_inlinks.txt"

        # test on file1
        file1 = "/Users/lijian/Dropbox/Courses/15Fall-Information Retrieval/homework 2/example.txt"

        # lines = [line.rstrip('\n').split() for line in open(file1)]
        f = open(file)
        lines = []
        for line in f:
            lines.append(line.split())
        print lines

        # print f.readline()
        # print f.readline()
        # print f.readline()
        # print type(f.readline())

        # print f
        # for line in f:
            # print type(line)
            # print line


        # print lines

a = Solution()
