# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 11:37:15 2019

@author: NEIL_YU
"""

import os, sys

try:
    sys.exit(0)
except:
    print('die')
finally:
    print('cleanup')

try:
    os._exit(0)
except:
    print('die')
print('os.exit')#不打印直接退出了