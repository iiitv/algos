"""
Implementation of gradient descent algorithm for minimizing cost of a linear hypothesis function.
"""
import numpy
from os.path import expanduser
import matplotlib.pyplot as plt


def _error(input_data, output_data, parameter_vector):
    """
    :param input_data:  Data whose summation of cost derivative has to be calculated
    :param output_data: Output corresponding to training data
    :param parameter_vector: Weight vector
    :return:
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


def summation_of_cost_derivative(input_data, output_data, parameter_vector):
    """
    Calculates the sum of cost function derivative
    :param input_data:  Data whose summation of cost derivative has to be calculated
    :param output_data: Output corresponding to training data
    :param parameter_vector: Weight vector

    :return: Returns the summation of cost derivative
    """
    return numpy.dot(input_data.transpose(), _error(input_data, output_data, parameter_vector))


def get_cost_derivative(train_data, train_output, parameter_vector):
    """

    :param train_data: Training data
    :param train_output: Output corresponding to training data
    :param parameter_vector: Weight vector
    :return: derivative vector
    """
    train_data_size = len(train_data)
    return summation_of_cost_derivative(train_data, train_output,
                                        parameter_vector)/train_data_size


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
        cost_derivative = get_cost_derivative(train_data, train_output, parameter_vector)
        temp_parameter_vector = parameter_vector - \
            learning_rate*cost_derivative
        if numpy.allclose(parameter_vector, temp_parameter_vector,
                          atol=absolute_error_limit, rtol=relative_error_limit):
            break
        parameter_vector = temp_parameter_vector
    return parameter_vector


def test_gradient_descent(test_data, test_output, parameter_vector):
    """
    :param test_data: Input data to be tested
    :param test_output: Actual Output data for Input dataset
    :param parameter_vector: Weight vector after optimized by using gradient descent
    :return: None
    """
    actual_output = test_output
    hypothesis_output = _hypothesis_value(test_data,
                                          parameter_vector=parameter_vector)
    num_examples = len(test_output)
    plt.stem(range(num_examples), actual_output, markerfmt='go', label='Actual Output')
    plt.stem(range(num_examples), hypothesis_output, label='Hypothesis Output')
    plt.xlabel('Test case')
    plt.ylabel('Output Values')
    plt.xlim([-1, 7])
    plt.legend()
    plt.show()


def download_data():
    """
    Downloads test and train data from GitHub repository
    """
    import requests
    home = expanduser('~')
    response = requests.get('https://github.com/iiitv/algos/blob/master/.datasets/'
                            'linear_regression/rock_aquifer_train.dat')
    if response:
        with open(home+'/rock_aquifer_train.dat', 'wb') as f:
            f.write(response.text)
    response = requests.get('https://github.com/iiitv/algos/blob/master/.datasets/'
                            'linear_regression/rock_aquifer_test.dat')
    if response:
        with open(home + '/rock_aquifer_test.dat', 'wb') as f:
            f.write(response.text)


def main():
    download_data()
    home = expanduser('~')
    input_cols = list(range(11))
    train_data = numpy.asmatrix(numpy.loadtxt(home + '/Documents/rock_aquifer_train.dat',
                                              usecols=input_cols))
    num_data = len(train_data)
    biased_tuple = numpy.asmatrix(numpy.ones((1, num_data), dtype=float).transpose())
    train_data = numpy.column_stack((biased_tuple, train_data))
    output_cols = (11,)
    train_output = numpy.asmatrix(numpy.loadtxt(home + '/Documents/rock_aquifer_train.dat',
                                                usecols=output_cols)).transpose()
    parameter_vector = numpy.asmatrix([2, 4, 1, 5, 4, 1, 2, 2, 3, 1, 1, 2]).transpose()
    learning_rate = 0.00015
    absolute_error_limit = 0.000015
    relative_error_limit = 0
    parameter_vector = run_gradient_descent(train_data, train_output, parameter_vector,
                                            learning_rate, absolute_error_limit,
                                            relative_error_limit)
    test_data = numpy.loadtxt(home + '/Documents/rock_aquifer_test.dat', usecols=input_cols)
    num_data = len(test_data)
    biased_tuple = numpy.asmatrix(numpy.ones((1, num_data), dtype=float).transpose())
    test_data = numpy.column_stack((biased_tuple, test_data))
    test_output = numpy.loadtxt(home + '/Documents/rock_aquifer_test.dat', usecols=output_cols)
    test_gradient_descent(test_data, test_output, parameter_vector=parameter_vector)


if __name__ == '__main__':
    main()
