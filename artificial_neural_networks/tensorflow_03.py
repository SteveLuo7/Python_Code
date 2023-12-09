import tensorflow as tf
def events_demo():
    with tf.compat.v1.Session() as sess:

        a = tf.constant(20,name='A')
        b = tf.constant(30,name='B')
        c = a + b

        print('c: ',c)

        c_value = sess.run(c)
        print('tesor_c: ',c_value)

        #   generate the events file
        writer = tf.compat.v1.summary.FileWriter('D:/events/test',graph=tf.compat.v1.get_default_graph())
        writer.close()



if __name__ == '__main__':
    events_demo()