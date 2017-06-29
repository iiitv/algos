"""
Linear regression is the most basic type of regression commonly used for
predictive analysis. The idea is preety simple, we have a dataset and we have
a feature's associated with it. The Features should be choose very cautiously
as they determine, how much our model will be able to make future predictions.
We try to set these Feature weights, over many iterations, so that they best
fits our dataset. In this particular code, i had used a CSGO dataset (ADR vs
Rating). We try to best fit a line through dataset and estimate the parameters.
"""

import sys
import requests
import numpy as np
import matplotlib.pyplot as plt


def collect_dataset():
    """ Collect dataset of CSGO
    The dataset contains ADR vs Rating of a Player
    :return : dataset obtained from the link, as matrix
    """
    response = requests.get('https://raw.githubusercontent.com/yashLadha/' +
                            'The_Math_of_Intelligence/master/Week1/ADRvs' +
                            'Rating.csv')
    lines = response.text.splitlines()
    data = []
    for item in lines:
        item = item.split(',')
        data.append(item)
    data.pop(0)  # This is for removing the labels from the list
    dataset = np.matrix(data)
    return dataset


def run_steep_gradient_descent(data_x, data_y,
                               len_data, alpha, theta):
    """ Run steep gradient descent and updates the Feature vector accordingly_
    :param data_x   : contains the dataset
    :param data_y   : contains the output associated with each data-entry
    :param len_data : length of the data_
    :param alpha    : Learning rate of the model
    :param theta    : Feature vector (weight's for our model)
    ;param return    : Updated Feature's, using
                       curr_features - alpha_ * gradient(w.r.t. feature)
    """
    n = len_data

    prod = np.dot(theta, data_x.transpose())
    prod -= data_y.transpose()
    sum_grad = np.dot(prod, data_x)
    theta = theta - (alpha / n) * sum_grad
    return theta


def sum_of_square_error(data_x, data_y, len_data, theta):
    """ Return sum of square error for error calculation
    :param data_x    : contains our dataset
    :param data_y    : contains the output (result vector)
    :param len_data  : len of the dataset
    :param theta     : contains the feature vector
    :return          : sum of square error computed from given feature's
    """
    error = 0.0
    prod = np.dot(theta, data_x.transpose())
    prod -= data_y.transpose()
    sum_elem = np.sum(np.square(prod))
    error = sum_elem / (2 * len_data)
    return error


def run_linear_regression(data_x, data_y):
    """ Implement Linear regression over the dataset
    :param data_x  : contains our dataset
    :param data_y  : contains the output (result vector)
    :return        : feature for line of best fit (Feature vector)
    """
    iterations = 100000
    alpha = 0.0001550

    no_features = data_x.shape[1]
    len_data = data_x.shape[0] - 1

    theta = np.zeros((1, no_features))

    for i in range(0, iterations):
        theta = run_steep_gradient_descent(data_x, data_y,
                                           len_data, alpha, theta)
        error = sum_of_square_error(data_x, data_y, len_data, theta)
        print('Error at %d iteration is : %.5f' % (i+1, error))

    return theta


def plot_data(data, output, theta):
    """ Visualisation of data
    :param data   : dataset for training
    :param output : output of training
    :param theta  : weights of model
    """

    data = np.asmatrix(data.transpose())
    x = np.asarray(data[1, :]).reshape(-1)
    y = np.asarray(output.transpose()).reshape(-1)
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(111)
    ax.scatter(x, y, label='actual-output')
    plt.plot(x, np.asarray(np.dot(theta, data)).reshape(-1),
             'r', label='predicted')
    plt.xlabel("Data value")
    plt.ylabel("output value")
    plt.legend()
    plt.show()


def main():
    """ Driver function """
    data = collect_dataset()

    len_data = data.shape[0]
    data_x = np.c_[np.ones(len_data), data[:, :-1]].astype(float)
    data_y = data[:, -1].astype(float)

    theta = run_linear_regression(data_x, data_y)
    if len(sys.argv) == 2:
        if sys.argv[1] == 'show-plot':
            plot_data(data_x, data_y, theta)


if __name__ == '__main__':
    main()
