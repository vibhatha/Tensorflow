import tensorflow as tf
import numpy as np
##############
## Lesson 1 ##
##############
#x = tf.constant(35, name='x')
#y = tf.Variable(x + 5, name='y')

#print(y)

# x = tf.constant(35, name='x')
# y = tf.Variable(x + 5, name='y')

# model = tf.global_variables_initializer()

# with tf.Session() as session:
#     session.run(model)
#     print(session.run(y))

##############
## Lesson 2 ##
##############

# x = tf.constant([35, 40, 45], name='x')
# y = tf.Variable(x + 5, name='y')


# model = tf.global_variables_initializer()

# with tf.Session() as session:
# 	session.run(model)
# 	print(session.run(y))

##############
## Lesson 3 ##
##############

# data = np.random.randint(1000, size=10000)
# data_tf = tf.Variable(data, name="data-ar")

# model = tf.global_variables_initializer()

# with tf.Session() as session:
# 	session.run(model)
# 	print(session.run(data_tf))

##############
## Lesson 4 ##
##############

# x = tf.Variable(0, name='x')

# model = tf.global_variables_initializer()

# with tf.Session() as session:
#     session.run(model)
#     for i in range(5):
#         x = x + 1
#         print(session.run(x))

##############
## Lesson 5 ##
##############

x = tf.constant(35, name='x')
print(x)
y = tf.Variable(x + 5, name='y')

with tf.Session() as session:
    merged = tf.summary.merge_all()
    writer = tf.summary.FileWriter("output_sgd_benchmark", session.graph)
    model =  tf.global_variables_initializer()
    session.run(model)
    session.run(y)
    print(session.run(y))

##############
## Lesson 6 ##
##############


##############
## Lesson 7 ##
##############


##############
## Lesson 8 ##
##############


##############
## Lesson 9 ##
##############


###############
## Lesson 10 ##
###############


###############
## Lesson 11 ##
###############

###############
## Lesson 12 ##
###############




        
