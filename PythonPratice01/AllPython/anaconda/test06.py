# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 15:52:15 2019

@author: NEIL_YU
"""

import time
import sys

ti=0.01
'''while True:
    for i in range(51):
        #sys.stdout.write('\r')
        #sys.stdout.write("[%-50s] %d%%" % ('='*i, 2*i))
        sys.stdout.write("\r[%-50s] %3d%%" % ('='*i, 2*i))
        sys.stdout.flush()
        time.sleep(ti)
        

    for i in range(51):
        sys.stdout.write("\r[%-50s] %3d%%" % ('='*(50-i), (100-2*i)))
        sys.stdout.flush()
        time.sleep(ti)'''
        

for i in range(1,1001):
    #i=int(i/1000*100)
    i=int(i/1000*100)
    sys.stdout.write("\r[%-50s] %3d%%" % ('='*int(i/2), i))
    sys.stdout.flush()
    time.sleep(ti)