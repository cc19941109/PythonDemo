
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
result1 = sess.run(hello)

a = tf.constant(10)
b = tf.constant(32)
result2 = sess.run(a + b)


sess.close()

print(result1)
print(result2)