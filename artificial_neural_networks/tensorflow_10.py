import tensorflow as tf

with tf.compat.v1.Session() as sess:
    x = tf.constant([10,20,30,40])
    y = tf.Variable(initial_value=x*20+10)
    #   initialize the value variable
    model = tf.compat.v1.global_variables_initializer()
    #   running the value variable
    sess.run(model)

    print('x: ',x)
    print('y: ',y)

    y_value = sess.run(y)
    print('y_value: \n',y_value)
