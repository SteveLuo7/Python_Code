import tensorflow as tf

def default_graph_demo():
    with tf.compat.v1.Session() as sess:
        a = tf.constant(10)
        b = tf.constant(20)
        c = a + b
        print('default pic: ',tf.compat.v1.get_default_graph())
        print('a_default_grpah: ',a.graph)
        print('b_default_grpah: ',b.graph)
        print('c_default_grpah: ',c.graph)


        c_value = sess.run(c)
        print('c_value: ', c_value)


if __name__ == '__main__':
    default_graph_demo()