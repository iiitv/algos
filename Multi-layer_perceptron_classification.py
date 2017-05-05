
from __future__ import print_function

#Here we are Directly using the MNIST dataset available in Tensorflow for training and testing

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

import tensorflow as tf 


# Create model with on hidden layer between input and output
def multilayer_perceptron(x, weights, biases):  
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)
    # Output layer with linear activation
    out_layer = tf.matmul(layer_1, weights['out']) + biases['out']
    return out_layer

def main():	
	learning_rate = 0.001 #Learning rate for the Descent and optimizatiom
	training_epochs = 15 #no of loops the training step runs
	batch_size = 100 # Size of code chunks used for training prpose
	display_step = 1 #Just a notion used to display each and every training steps details. 
	n_hidden_1 = 256 # 1st layer number of features
	n_input = 784 # MNIST data input (img shape: 28*28)
	n_classes = 10 # MNIST total classes (0-9 digits)

	# Tensorflow Graph input of placeholder type
	x = tf.placeholder("float", [None, n_input])
	y = tf.placeholder("float", [None, n_classes])

	# Weights and Biases are defined over here.
	weights = {
	    'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
	    'out': tf.Variable(tf.random_normal([n_hidden_1, n_classes]))
	}
	biases = {
	    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
	    'out': tf.Variable(tf.random_normal([n_classes]))
	}

	# Construct model " Generally the Calculation using all values"
	pred = multilayer_perceptron(x, weights, biases)

	# Define loss and optimizer ( Here we are using Adam optimizer and Loss function is not exactly cross entropy function, but another version of it 		"softmax_cross_entropy_with_logits of tensorflow library"
	cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
	optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

	# Initializing the variables (this initialises all variable types)
	init = tf.global_variables_initializer()

	# Launch the graph
	with tf.Session() as sess:
	    sess.run(init)
	
	    # Training cycle
	    for epoch in range(training_epochs):
	        avg_cost = 0.
	        total_batch = int(mnist.train.num_examples/batch_size)
	        # Loop over all batches
	        for i in range(total_batch):
	            batch_x, batch_y = mnist.train.next_batch(batch_size)
	            _, c = sess.run([optimizer, cost], feed_dict={x: batch_x,y: batch_y})
	            avg_cost += c / total_batch
	        if epoch % display_step == 0:
	            print("Epoch:", '%04d' % (epoch+1), "cost=", \
	                "{:.9f}".format(avg_cost))
	    print("Optimization Finished!")
	
	    # Test model by checking y_pred with y _given
	    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
	    # Calculate accuracy
	    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
	    print("Accuracy:", accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))

if __name__ == '__main__':
    main()
