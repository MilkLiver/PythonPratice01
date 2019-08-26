# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 08:46:55 2019

@author: NEIL_YU
"""

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))