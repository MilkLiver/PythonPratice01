# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 16:01:58 2019

@author: NEIL_YU
"""

import tensorflow as tf


matrix1=tf.constant([[3,3]])
matrix2=tf.constant([[2],[2]])
matrix3=tf.constant([[4,4]])
product=tf.matmul(matrix1,matrix2)
product=tf.matmul(product,matrix3)

# method 1
sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()
# [[12]]

# method 2
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)
# [[12]]
