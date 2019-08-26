# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 09:16:51 2019

@author: NEIL_YU
"""


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import os
import numpy as np
import tensorflow as tf


# Data sets
CAR_TRAINING = "car_labels.csv"
CAR_TEST = "car_labels.csv"

def main():
    # If the training and test sets aren't stored locally, download them.
    if not os.path.exists(CAR_TRAINING):
        print(CAR_TRAINING,"Not Found")
        exit()
      
    if not os.path.exists(CAR_TEST):
        print(CAR_TEST,"Not Found")
        exit()
    
    training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
            filename=CAR_TRAINING,target_dtype=np.int,
            features_dtype=np.float32)
     
    test_set = tf.contrib.learn.datasets.base.load_csv_with_header(
            filename=CAR_TEST,target_dtype=np.int,
            features_dtype=np.float32)
    
    
if __name__=="__main__":
    main()
    print("OwO")
      
