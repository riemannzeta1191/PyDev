import threading
import logging
import random
import time
import  Queue, sys


Buff_Size = 10
q = Queue.Queue(Buff_Size)
_sentinel = object()

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)


class Producer(threading.Thread):
    def  __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(Producer, self).__init__(group=None)
        self.name = name
        self.target = target
        self.running = True

    def run(self):
        while self.running:
            if not q.full():
                item  = random.randint(1, 10)
                q.put(item)
                logging.debug('Putting ' + str(item)
                              + ' : ' + str(q.qsize()) + ' items in queue')
                time.sleep(1)
            elif q.qsize() == 0:
                q.put(None)
                self.running = False

        return

class Consumer(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(Consumer, self).__init__(group=None)
        self.name = name
        self.target = target
        self.producer_alive = True

    def run(self):
        while self.producer_alive:
            if not q.empty():
                item = q.get()
                # if item is _sentinel:
                #     q.put(_sentinel)
                #     break
                logging.debug('Getting ' + str(item)
                              + ' : ' + str(q.qsize()) + ' items in queue')
                time.sleep(random.random())
            elif q.qsize() is 0:
                q.put(None)
                self.producer_alive =False
                logging.debug("Producer is gone...")
                sys.exit(1)


        return

if __name__=="__main__":
    p = Producer(name="Producer")
    c = Consumer(name="Consumer")

    # p.setDaemon(True)
    logging.debug("Starting..")
    p.setDaemon(True)
    p.start()



    time.sleep(10)

    c.start()
    logging.debug("Consumer Starting..")












