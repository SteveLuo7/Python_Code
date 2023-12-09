import tensorflow as tf
def add_demo():
    with tf.compat.v1.Session() as sess:
        a = 10
        b = 20
        c = a + b
        print('Orignial Python: ',c)

        a_t = tf.constant(10)
        b_t = tf.constant(20)
        print('a_t: ',a_t)
        c_t = a_t + b_t
        print('Tensorflow: ',c_t)

        #   with session

        print('c_t_value: ',sess.run(c_t))

if __name__ == '__main__':
    add_demo()