import tensorflow as tf


state = tf.Variable(0,name="counter")
print(state.name)

one = tf.constant(1)

new_value = tf.add(state,one)

update = tf.assign(state,new_value)

# important!
# must have if define variable
init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    for x in range(3):
        sess.run(update)
        # 直接 print(stata) 不行
        print(sess.run(state))
