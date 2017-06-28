"""
To view the plot, run as follows:
python3 gradient_descent.py show-plot
Implementation of gradient descent algorithm for minimizing cost of a linear hypothesis function.
"""
import numpy
import requests
import matplotlib.pyplot as plt
import sys


def _error(input_data, output_data, parameter_vector):
    """
    :param input_data:  Data whose summation of cost derivative has to be calculated
    :param output_data: Output corresponding to training data
    :param parameter_vector: Weight vector
    :return: Error in hypothesis value
    """
    return _hypothesis_value(input_data, parameter_vector) - output_data


def _hypothesis_value(data, parameter_vector):
    """
    Calculates hypothesis function value for a given data
    :param data: Data whose hypothesis value has to be calculated
    :param parameter_vector: Weight vector
    :return: Vector of values of hypothesis function for given data matrix.
    """
    return numpy.asmatrix(numpy.dot(data, parameter_vector))


def get_cost_derivative(input_data, output_data, parameter_vector):
    """
    :param input_data: Training or testing data
    :param output_data: Output corresponding to training data
    :param parameter_vector: Weight vector
    :return: derivative vector
    """
    train_data_size = len(input_data)
    return numpy.dot(input_data.transpose(), _error(input_data, output_data, parameter_vector))\
        / train_data_size


def run_gradient_descent(train_data, train_output, parameter_vector,
                         learning_rate, absolute_error_limit,
                         relative_error_limit):
    """
    Runs gradient descent on given training data and optimizes
    parameters
    :param train_data: Training data. Type: Matrix.
    :param train_output: Output corresponding to each training data. Type: Vector,
    may be matrix
    :param parameter_vector: Randomly initialized weight vector
    :param learning_rate: Rate at which gradient descent learns
    :param absolute_error_limit: Tolerance for error in training.
    :param relative_error_limit: Tolerance for error in training. It is relative to second parameter.
    :return: Optimized parameter vector.
    """
    while True:
        cost_derivative = get_cost_derivative(
            train_data, train_output, parameter_vector)
        temp_parameter_vector = parameter_vector - \
            learning_rate*cost_derivative
        if numpy.allclose(parameter_vector, temp_parameter_vector,
                          atol=absolute_error_limit, rtol=relative_error_limit):
            break
        parameter_vector = temp_parameter_vector
    return parameter_vector


def test_gradient_descent(input_data, output_data, parameter_vector):
    """
    :param input_data: Input data to be tested
    :param output_data: Actual Output data for Input dataset
    :param parameter_vector: Weight vector after optimized by using gradient descent
    :return: None
    """
    actual_output = output_data
    hypothesis_output = _hypothesis_value(input_data,
                                          parameter_vector=parameter_vector)
    if len(sys.argv) == 2:
        if sys.argv[1] == 'show-plot':
            num_examples = len(output_data)
            plt.plot(range(num_examples), actual_output,
                     'r', label='Actual Output')
            plt.plot(range(num_examples), hypothesis_output,
                     'g', label='Hypothesis Output')
            plt.xlabel('Test example')
            plt.ylabel('Output Values')
            plt.xlim([-1, len(input_data) + 2])
            plt.ylim([-5, 200])
            plt.legend()
            plt.show()


def download_data():
    """
    Downloads test and train data from GitHub repository
    """
    response = requests.get(
        'http://www.stat.ufl.edu/~winner/data/rock_aquifer.dat')
    train_data = []
    train_output = []
    data_matrix = response.text.split('\n')
    for data_tuple in data_matrix:
        data_tuple = data_tuple.split()
        if data_tuple:
            train_data.append(data_tuple[:11])
            train_output.append(data_tuple[-1])
    return numpy.asmatrix(train_data).astype(dtype='float'), \
        numpy.asmatrix(train_output).astype(dtype='float')


def main():
    train_data, train_output = download_data()
    num_data = len(train_data)
    biased_tuple = numpy.asmatrix(numpy.ones(
        (1, num_data), dtype=float).transpose())
    train_data = numpy.column_stack((biased_tuple, train_data))
    train_output = train_output.transpose()
    parameter_vector = numpy.asmatrix(
        [2, 4, 1, 5, 4, 1, 2, 2, 3, 1, 1, 2]).transpose()
    learning_rate = 0.00015
    absolute_error_limit = 0.000015
    relative_error_limit = 0
    parameter_vector = run_gradient_descent(train_data, train_output, parameter_vector,
                                            learning_rate, absolute_error_limit,
                                            relative_error_limit)
    test_gradient_descent(train_data, train_output,
                          parameter_vector=parameter_vector)


if __name__ == '__main__':
    main()
