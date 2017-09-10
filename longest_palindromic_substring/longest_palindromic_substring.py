def expand_around_center(test, left, right):
    """
    :param test: Input string whose substrings are to be checked
    :param left: Left end of result palindromic substring
    :param right: Right end of result palindromic substring
    :return: Length of palindromic substring
    """
    n = len(test)
    while left >= 0 and right < n and test[left] is test[right]:
        left -= 1
        right += 1
    return right - left - 1


def longest_palindromic_substring(test):
    """
    Function to find longest substring which is a palindrome

    :param test: Input string whose substrings are to be checked
    :return: Longest substring of input string which is a palindrome

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    start = end = 0
    for i in range(len(test)):
        length = max(expand_around_center(test, i, i),
                     expand_around_center(test, i, i + 1)
                     )
        if length > end - start:
            start = i - (length - 1) // 2
            end = i + length // 2
    return test[start: end + 1]


def main():
    """
    Driver function to test the code.
    """
    test = 'geeksforgeeks'
    print('Longest palindromic substring of', test,
          'is', longest_palindromic_substring(test))


if __name__ == '__main__':
    main()
