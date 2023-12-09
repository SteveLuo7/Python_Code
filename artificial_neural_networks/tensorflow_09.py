import tensorflow as tf

with tf.compat.v1.Session() as sess:
    A = tf.constant([[1,2,3],[4,5,6]])
    B = tf.fill([3,4],3)

    A_value = sess.run(A)
    B_value = sess.run(B)

    print('A_value: \n',A_value)
    print('B_value: \n',B_value)

    matmal = tf.matmul(A,B)
    print('matmal: \n',sess.run(matmal))
