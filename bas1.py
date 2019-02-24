import tensorflow as tf

a = tf.constant(5)
b = tf.constant(6)

res = tf.multiply(a,b)
sess = tf.get_session_tensor()
print(sess.run(res))