import collections
import numpy
import requests


TRAIN_RATIO = 0.8


def k_nn(train_x, train_y, test_x, k):
    """
    Predicts the class of given data point using k-NN algorithm
    :param train_x: Features of training dataset
    :param train_y: Class of training dataset
    :param test_x: Featues of testing data point
    :param k: Value of 'k' in k-NN algorithm
    :return: Predicted class of test_x
    """
    # Calculate the distance of current point from all other points.
    # Complexity: O(nf), where f is number of features
    dist = numpy.sqrt(sum(numpy.square(train_x - test_x).T)).T
    # Add labels with corresponding distances
    dist_with_label = numpy.hstack([train_y, dist]).T
    # Get index of smallest k elements. Complexity: O(n + klog(k))
    dist_with_label_sorted = numpy.argpartition(dist_with_label, -k).T[:k]
    # Arrange 'dist_with_label' according to sorted index of distance
    inter = dist_with_label[:, dist_with_label_sorted[:, 1]].reshape([2, k])
    # Get the top labels in 1D array
    top_labels = numpy.asarray(inter[0]).reshape([k])
    # Get the most common neighbor. Complexity: O(k)
    k_nn_label = collections.Counter(top_labels).most_common(1)[0][0]
    return k_nn_label


def load_iris_data(shuffle=False):
    """
    Loads iris dataset from internet
    :param shuffle: True will result in shuffling of dataset
    :return: Tuple of features and corresponding classes from iris dataset
    """
    req = requests.get('https://archive.ics.uci.edu/'
                       'ml/machine-learning-databases/'
                       'iris/iris.data')
    req_html = req.text
    data_str = req_html.strip().split('\n')
    data = []
    for item in data_str:
        item = item.split(',')
        data.append(item)
    data = numpy.matrix(data)
    if shuffle:
        numpy.random.shuffle(data)
    data_x = data[:, :-1].astype(float)
    data_y = data[:, -1]
    return data_x, data_y


def k_nn_test(tr_x, tr_y, te_x, te_y, k):
    """
    Tests the k-NN algorithm for given dataset and returns error ratio
    :param tr_x: Features of training dataset
    :param tr_y: Class of training dataset
    :param te_x: Features of testing dataset
    :param te_y: Actual class of testing dataset
    :param k: Value of "k" in k-NN algorithm
    :return: Error ratio for given dataset and model
    """
    test_size = len(te_x)
    error = 0.
    for i in range(test_size):
        x = te_x[i]
        y_actual = te_y[i]
        y_predicted = k_nn(tr_x, tr_y, x, k)
        if y_actual != y_predicted:
            error += 1
    return error / test_size


def main():
    data_x, data_y = load_iris_data(shuffle=True)

    # Calculate size of train and test partitions
    train_size = int(len(data_x) * TRAIN_RATIO)
    test_size = len(data_x) - train_size

    # Generate train and test partitions
    train_x, train_y = data_x[:train_size], data_y[:train_size]
    test_x, test_y = data_x[test_size + 1:], data_y[test_size + 1:]

    # Test for error
    error_ratio = k_nn_test(train_x, train_y, test_x, test_y, 7)
    print(error_ratio)


if __name__ == '__main__':
    main()
