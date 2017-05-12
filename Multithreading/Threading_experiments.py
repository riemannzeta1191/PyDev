import threading, math
from multiprocessing import Process



#
# Py_BEGIN_ALLOW_THREADS
#     sleep((int)secs);      A thread can bypass the GIL by releasing it when it enters a I/O blocking
# Py_END_ALLOW_THREADS       instruction,during which other threads can run in parallel untill is asks
#                            back the GIL.Cpython interpreter only allows a thread at a time not the memory
#                            which can spawn n number of threads using the os-kernel.But spawning itself
#                            is a memory consuming process and thus multithreading is a performance degenerating
#                            feature in python.In contrast to the performance GIL protects the shared resources
#                            to not vanish into aether as it hinders threads to decrease the ref count of the
#                            shared object to not become 0 ,which in turn would lead to the garbage allocation of
#                            the object called by the interpreter using __del__ built_in method.GIL primarily
#                            helps in memory management within the call stack and the objects in the heap.Ideally
#                            it's not a feature for the end user's routine use.

def non_threaded():
    return prime_range(1,100)

def threaded():
    t1  = threading.Thread(name="threaded-1",target=prime_range,args=(1,20))
    t2  = threading.Thread(name="threaded-2",target=prime_range,args=(21,40))
    t3  = threading.Thread(name="threaded-3",target=prime_range,args=(41,60))
    t4  = threading.Thread(name="threaded-4",target=prime_range,args=(61,80))
    t5  = threading.Thread(name="threaded-5",target=prime_range,args=(81,100))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
#
# --------Results--------
# ('Non threaded Duration: ', 0.00012200000000000405, 'seconds')   for 2 threads
# ('Threaded Duration: ', 0.0014069999999999985, 'seconds')

    #Multithreading if it's CPU bound job becomes very costly for the Cpython since all threads wait
    #for each other to complete in addition to the overhead of spawning new threads.One processor
    #at a time should be acting upon one thread and carrying on the work.

# --------Results--------
# ('Non threaded Duration: ', 0.0001250000000000001, 'seconds')   for 3 threads
# ('Threaded Duration: ', 0.004196999999999999, 'seconds')


# --------Results--------
# ('Non threaded Duration: ', 0.0003919999999999965, 'seconds')   for 5 threads
# ('Threaded Duration: ', 0.007214999999999999, 'seconds')
#

    print ("Finishing Catalan...")

def catalan_number(num):
    if num <= 1:
        return 1

    res_num = 0
    for i in range(num):
        res_num += catalan_number(i) * catalan_number(num-i-1)
        return res_num

def catalan_num_range(m,n):
    k = (n-m)
    for i in range(k):
        print catalan_number(i),



def is_prime(n):
    if n>2 and n%2==0:
        return False
    for i in range(3, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
        return True

def prime_range(m,n):
    k = n-m
    l = []
    for i in range(k):
        if is_prime(i):
            l.append(i)





if __name__ == '__main__':
    import time
    print("--------Nonthreaded calculation--------")
    nTstart_time = time.clock()
    non_threaded()
    nonThreadedTime = time.clock() - nTstart_time

    print("--------Threaded calculation--------")

    Tstart_time = time.clock()
    threaded()
    threadedTime = time.clock() - Tstart_time

    print("--------Results--------")
    print ("Non threaded Duration: ",nonThreadedTime, "seconds")
    print ("Threaded Duration: ",threadedTime, "seconds")

