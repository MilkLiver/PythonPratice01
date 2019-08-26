import multiprocessing
import time
import os

def work(ttime=1):
    print(ttime)
    ttime=5
    time.sleep(ttime)
    print('child process end')
    
a=[1,2,3]
if __name__=="__main__":
    
    #p1 = multiprocessing.Process(target=work)
    #p1.start()
    #p1.join()
#-----------------------------------------------------------------
    poolnum=5
    thpool=multiprocessing.Pool(poolnum)
    for i in range(7):
        thpool.apply_async(work)
        thpool=multiprocessing.Pool(poolnum)
        print(os.getpid)

    


#-----------------------------------------------------------------
    time.sleep(5)
    thpool.close()
    print(os.getpid)
    print(multiprocessing.cpu_count())
    #print(p1.name,p1.pid)
    print('main process end')


