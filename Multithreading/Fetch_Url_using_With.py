import threading, urllib2,logging,time
class Fetch_Url(threading.Thread):
    def __init__(self, urls, output, lock):
        threading.Thread.__init__(self)
        self.urls = urls
        self.output = output
        self.lock = lock


    def run(self):
        while self.urls:
            url = self.urls.pop()
            req = urllib2.Request(url)
            d = urllib2.urlopen(req)
            with self.lock:
                print 'lock acquired by %s' % self.name
                self.output.write(d.read())
                print 'write done by %s' % self.name
                print 'lock released by %s' % self.name
                # print 'URL %s failed: %s' %self.urls %self.urls
                self.output.write(d.read())
                print 'write done by %s' % self.name
                print 'URL %s fetched by %s' % (url, self.name)


def main():

    # list 1 of urls to fetch

    urls2 = ['http://www.google.com', 'http://www.facebook.com']

    # list 2 of urls to fetch

    urls1 = ['http://www.yahoo.com', 'http://www.youtube.com']

    f = open('output_with.txt', 'w+')

    lock = threading.RLock()

    t1 = Fetch_Url(urls1, f, lock)

    t2 = Fetch_Url(urls2, f, lock)

    t1.start()
    print ("Thread-1 Starting...")
    time.sleep(10)

    t2.start()
    print ("Thread-2 Starting...")

    t1.join()

    t2.join()

    f.close()


if __name__=="__main__":
    main()











# while self.urls:
# 22
#             url = self.urls.pop()
# 23
#             req = urllib2.Request(url)
# 24
#             try:
# 25
#                 d = urllib2.urlopen(req)
# 26
#             except urllib2.URLError, e:
# 27
#                 print 'URL %s failed: %s' % (url, e.reason)
# 28
#             self.output.write(d.read())
# 29
#             print 'write done by %s' % self.name
# 30
#             print 'URL %s fetched by %s' % (url, self.name)
