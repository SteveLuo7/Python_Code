import tensorflow as tf
def tensor_shape_demo():
    with tf.compat.v1.Session() as sess:
        a_p = tf.compat.v1.placeholder(dtype=tf.float32,shape=[None,None])
        b_p = tf.compat.v1.placeholder(dtype=tf.float32,shape=[None,5])
        c_p = tf.compat.v1.placeholder(dtype=tf.float32,shape=[3,4])
        print('Modify constant ')
        print('a_p: ',a_p)
        # a_p.set_shape([3,4])
        a_p.set_shape([2,5])
        print('a_p_modified: ',a_p)

        b_p.set_shape([5,5])
        print('b_p: ',b_p)

        #   modify must be sure the same elements
        print('c_p: ',c_p)
        c_p1 = tf.compat.v1.reshape(c_p,shape=[2,6])
        print('c_p1: ',c_p1)

if __name__ == '__main__':
    tensor_shape_demo()