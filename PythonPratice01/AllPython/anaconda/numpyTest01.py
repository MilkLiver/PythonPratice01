# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 11:02:17 2019

@author: NEIL_YU
"""

import os
import sys
import datetime as dt
import numpy as np



def main(argc,argv,envp):
    a=np.arange(1,10).reshape(3,3)
    b=a*10
    print(a,b,sep='\n')
    print(a.transpose())
    print(a.transpose().transpose())
    print(a.transpose()[0])
    print(a.transpose()[1])
    print(a.T)
    
    return 0

if __name__=="__main__":
    #sys.exit(main(len(sys.argv),sys.argv,os.environ))
    main(len(sys.argv),sys.argv,os.environ)