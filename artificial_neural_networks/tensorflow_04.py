import tensorflow as tf

def session_demo():
    with tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(allow_soft_placement=True,
                                                              log_device_placement=True)) as sess:
        a = tf.constant(20)
        b = tf.constant(30)
        c = a + b
        print('c: ',c)

        c_tensor = sess.run(c)
        print('c_tensor: ',c_tensor)


if __name__ == '__main__':
    session_demo()