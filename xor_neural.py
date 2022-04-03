import tensorflow.compat.v1 as tf
print(tf.version)

tf.compat.v1.disable_eager_execution()

# input X vector
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
# output Y vector
Y = [[0], [1], [1], [0]]

# Placeholders for input and output
x = tf.placeholder(dtype=tf.float32, shape=[4, 2])
y = tf.placeholder(dtype=tf.float32, shape=[4, 1])

# W matrix
W1 = tf.Variable([[1.0, 0.0], [1.0, 0.0]], shape=[2, 2])
W2 = tf.Variable([[0.0], [1.0]], shape=[2, 1])

# Biases
B1 = tf.Variable([0.0, 0.0], shape=[2])
B2 = tf.Variable([0.0], shape=1)

# Hidden layer and outout layer
output = tf.sigmoid(tf.matmul(tf.sigmoid(tf.matmul(x, W1) + B1), W2) + B2)

# error estimation
e = tf.reduce_mean(tf.squared_difference(y, output))
train = tf.train.GradientDescentOptimizer(0.1).minimize(e)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in range(100001):
    error = sess.run(train, feed_dict={x: X, y: Y})
    if i % 10000 == 0:
        print('\nEpoch: ' + str(i))
        print('\nError: ' + str(sess.run(e, feed_dict={x: X, y: Y})))
        for el in sess.run(output, feed_dict={x: X, y: Y}):
            print('    ', el)
sess.close()

print("Complete")
