# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 11:32:53 2019

@author: NEIL_YU
"""

import pymysql

db=pymysql.connect(
        host="127.0.0.1",
        port=1433,
        user="OAO",
        passwd="Admin12345",
        db="OwO"
        )