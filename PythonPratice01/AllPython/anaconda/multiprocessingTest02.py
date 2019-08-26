# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:44:33 2019

@author: NEIL_YU
"""

import multiprocessing as mp
import os 



def show(i):
    print(i)
    
def main():
    #ml=mp.Lock()
    ml=mp.Manager().Lock()  
    qu=mp.Manager().Queue()
    pool=mp.Pool(processes=3)
    for i in os.listdir(r"D:\PyAI3\4\Annotations"):
        pool.apply_async(show,args=(i,))
        
    
    pool.close()
    pool.join()

if __name__=="__main__":
    main()