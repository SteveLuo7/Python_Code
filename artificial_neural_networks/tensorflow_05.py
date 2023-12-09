import tensorflow as tf

def session_demo():
    with tf.compat.v1.Session() as sess:
        a = tf.constant(20)
        b = tf.constant(30)
        c = a + b
        print('c: ',c)

        c_tensor = sess.run(c)
        print('c_tensor: ',c_tensor)

        #   send to list
        print('SEND INTO LIST ---------------------------------')
        v = sess.run([a,b,c])
        print('LIST: ',v)

        #   send into tuple
        print('SEND INTO TUPLE-----------------------------------')
        a_value,b_value,c_value = sess.run((a,b,c))
        print('a_value: {}, b_value: {}, c_value: {}'.format(a_value,b_value,c_value))

if __name__ == '__main__':
    session_demo()