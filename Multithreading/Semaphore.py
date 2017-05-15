import threading
import random
import time,logging


logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)



class myThread(threading.Thread):
    def __init__(self, count=0,group=None, target=None,args=(), kwargs=None,
			              name=None, verbose=None):
        super(myThread, self).__init__(group=None, target=None,args=(), kwargs=None,
			              name=None, verbose=None)
        self.var = count
        self.args = args
        self.kwargs = kwargs
        self.items = []
        self.semaphore = threading.Semaphore()
        self.lock = threading._RLock()

    def run(self):
        logging.debug("Starting %s" %self.name)

        while not len(self.items):
            self.semaphore.acquire()
            logging.debug("semaphore acquired by %s" %self.name)
            self.var  += 1
            self.items.append(self.var)
            logging.debug("Var incremented: %s" %self.var)
            self.semaphore.release()
            logging.debug("The len of list is %s" %len(self.items))
            logging.debug("Exiting %s" %self.name)
            return




if __name__=="__main__":
    t1 = myThread(name="Thread-1")
    t2 = myThread(name="Thread-2")
    t1.start()
    logging.debug("thread 1 starting")
    t2.start()
    logging.debug("thread 2 starting")
    t1.join()
    t2.join()

