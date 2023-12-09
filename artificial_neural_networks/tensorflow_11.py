import tensorflow as tf
def liner_regression():
    with tf.compat.v1.Session() as sess:
        X = tf.compat.v1.random_normal(shape=[100,1])
        y_true = tf.matmul(X,[[0.8]])+0.7

        weight = tf.Variable(initial_value=tf.compat.v1.random_normal(shape=[1,1]))
        bias = tf.Variable(initial_value=tf.compat.v1.random_normal(shape=[1,1]))
        y_predict = tf.matmul(X,weight) + bias

        error = tf.reduce_mean(tf.square(y_predict-y_true))
        optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.01).minimize(error)

        init = tf.compat.v1.global_variables_initializer()

        sess.run(init)
        print('befor the train:\n weight {}, \n bias {},\n error {}'.format(weight,bias,error))

        for i in range(100):
            sess.run(optimizer)
            print('after the train {} times :\n weight {}, \n bias {},\n error {}'.format(i,weight.eval(),bias.eval(),error))




if __name__ == '__main__':
    liner_regression()


