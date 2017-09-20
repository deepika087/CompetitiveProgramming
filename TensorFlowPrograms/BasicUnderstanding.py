__author__ = 'deepika'

import tensorflow as tf
deep_learning = tf.constant('Deep Learning')

session = tf.Session()
print session.run(deep_learning)

a = tf.constant(2)
b = tf.constant(3)
multiply = tf.run(a, b)
print session.run(multiply)

matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.],[2.]])
product = tf.matmul(matrix1, matrix2)
print product