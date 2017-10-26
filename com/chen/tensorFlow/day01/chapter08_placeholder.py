import tensorflow as tf

# 给定 type ,tf 中一般都是用 float32
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

# 原视频中为 tf.mul(input1,input2)
output = tf.multiply(input1,input2)

with tf.Session() as sess:
    print(sess.run(output,feed_dict={input1:[7.0],input2:[2.0]}))



