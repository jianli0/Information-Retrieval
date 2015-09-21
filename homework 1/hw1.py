import urllib
import time
from bs4 import BeautifulSoup

# frontier is a Queue
class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0,item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0


# initial
class Web_Crawl:
    def __init__(self):
        # used for crawling
        self.start_seed = "http://en.wikipedia.org/wiki/Hugh_of_Saint-Cher"
        self.start_depth = 1
        self.frontier = Queue()
        self.frontier.push([self.start_seed, self.start_depth])
        self.visited = []
        self.visited.append(self.start_seed)
        self.page_limit = 1000
        self.depth_limit = 5

        self.outputfile = r"/Users/lijian/"
        self.Main_Page = r"/wiki/Main_Page"

        # with respect to robots.txt

    def crawl_web(self):
        while not self.frontier.isEmpty() and self.page_limit >= 0:
            [current_seed, current_depth]= self.frontier.pop()
            # add prefix
            prefix = "https://en.wikipedia.org"
            if current_depth > 1:
                current_seed = prefix + current_seed
            if current_depth <= self.depth_limit:
                # be polite : with respect to robots.txt
                if self.approvedSites(current_seed):
                    # urllib : read the html content

                    # debug
                    # print "now crawling %r"%(current_seed)
                    # print type(current_seed)
                    url = urllib.urlopen(current_seed)
                    html = url.read()

                    # delay at least one second
                    time.sleep(1)

                    # beautiful soup to parse all the href
                    soup = BeautifulSoup(html)

                    # finding next seeds
                    for a in soup.find_all('a', href = True):
                        next_seed = a['href']
                        if self.valid_link(next_seed) and next_seed not in self.visited:
                            self.frontier.push([next_seed,current_depth + 1])
                            # add to visit list
                            self.visited.append(next_seed)
                            self.page_limit -= 1
                    # debug
                    # for i in self.visited:
                        # print i[:]

    def approvedSites(self,link):
        try:
            rp = robotparser.RobotFileParser()
            rp.set_url(link)
            rp.read()
            apSite = rp.apSite("*", link)
        except:
            apSite = True
        return apSite

    # valid_links :
    # start with the prefix http://en.wikipedia.org
    # do not follow links to main page and with more than one ":"

    # input: a link, "http://en.wikipedia.org/wiki/Main_Page"
    # output: Boolean, true or false
    def valid_link(self, link):
        if len(link) >= len("/wiki/") and link[:6] == "/wiki/":
            if not link == self.Main_Page:
                if link.count(":") == 0:
                    return True
        return False



    # write my two lists to a file, .txt maybe

    def writetofile(self):
        # remains to be done
        prefix = "https://en.wikipedia.org"
        self.crawl_web()
        for i in self.visited:
            print  prefix + i
        print "total webpage is %d"%len(self.visited)

#executing the program
if __name__ == '__main__':
    a = Web_Crawl()
    a.writetofile()

