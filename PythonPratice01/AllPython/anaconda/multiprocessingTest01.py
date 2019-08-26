# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 10:18:30 2019

@author: NEIL_YU
"""

import multiprocessing as mp
import os 


def GetAndWriteName(file_name,mplock=None):
    mplock.acquire()
    with open(r"D:\test\test.txt","a+") as te:
        te.write("test"+str(file_name)+"\n")
        te.close()
    mplock.release()

def main():
    #ml=mp.Lock()
    ml=mp.Manager().Lock()  
    qu=mp.Manager().Queue()
    pool=mp.Pool(processes=3)
    for i in os.listdir(r"D:\PyAI3\4\Annotation"):
        print(i)
        pool.apply_async(GetAndWriteName,args=(i,ml,))
        
    
    pool.close()
    pool.join()

if __name__=="__main__":
    main()