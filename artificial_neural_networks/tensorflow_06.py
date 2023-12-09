import tensorflow as tf

def default_session_demo():
    with tf.compat.v1.Session() as sess:
        a = tf.compat.v1.placeholder(tf.float32)
        b = tf.compat.v1.placeholder(tf.float32)
        c = a + b

        cc = tf.add(a,5)

        x = tf.compat.v1.placeholder(tf.float32,None)
        y = x * 20 + 100



        c_value = sess.run(c,{a:20,b:30})
        print('c_value: ',c_value)

        cc_value = sess.run(cc,{a:15})
        print('cc_value: ',cc_value)

        y_value = sess.run(y,{x:10})
        print('v_value: ',y_value)

        y_value_list = sess.run(y,{x:[1,2,3,4,5]})
        print('y_value_list',y_value_list)

if __name__ == '__main__':
    default_session_demo()