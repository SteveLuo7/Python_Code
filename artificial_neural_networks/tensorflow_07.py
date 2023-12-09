import tensorflow as tf
def tensor_demo():
    with tf.compat.v1.Session() as sess:
        #   constant tensor
        print('Create constant tensor')
        tensor1 = tf.constant(3.5)
        print('Tensor1: ',tensor1)
        tensor2 = tf.constant([1,2,3,4,5])
        print('Tensor2: ',tensor2)
        tensor3 = tf.constant([[1,2,3],[4,5,6]])
        print('Tensor3: ',tensor3)

        #   random tensor
        print('Create Random Tensor ')
        t_ones = tf.ones(shape=[2,3])
        t_zeros = tf.zeros(shape=[3,4])

        print('t_ones: ',t_ones)
        print('t_zeros: ',t_zeros)

        t_ones_value = sess.run(t_ones)
        print('t_ones_value: ',t_ones_value)

        t_zeros_value = sess.run(t_zeros)
        print('t_zeros_value: ',t_zeros_value)

        t_uniform = tf.compat.v1.random_uniform(shape=[1,2],minval=1,maxval=4)
        t_uniform_value = sess.run(t_uniform)
        print('t_uniform: ',t_uniform_value)

if __name__ == '__main__':
    tensor_demo()