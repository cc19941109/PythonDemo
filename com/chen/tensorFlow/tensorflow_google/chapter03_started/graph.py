import tensorflow as tf

a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0, 3.0], name='b')
result = a + b

sess = tf.Session()
x = sess.run(result)
print(x)

print(result)
print(a.graph is tf.get_default_graph())
