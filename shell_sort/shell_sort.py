def shell_sort(array):
    """
    Sorts the given array of integers using the Shell Sort algorithm
    Time Complexity : O((len(array))^2)
    Space Complexity : O(len(array))
    :param array: A List of integers.
    :return: returns the array sorted
    """

    # calculate the gap using Knuth's formula
    gap = 1
    while gap < len(array) // 3:
        gap = (gap * 3) + 1

    while gap > 0:
        # using this gap, exchange elements while you can
        for idx in range(gap, len(array)):
            val_to_insert = array[idx]
            candidate_idx = idx

            # shift all bigger elements to the right, creating a hole
            while candidate_idx > gap - 1 and array[candidate_idx - gap] > val_to_insert:
                array[candidate_idx] = array[candidate_idx - gap]
                candidate_idx -= gap

            # insert our element at the hole
            array[candidate_idx] = val_to_insert

        # decrease gap, math alert
        gap = (gap - 1) // 3

    return array


def main():
    sample_arr = [1, -312, 4, 12, 3, 17, 2542, 20, 18]
    print(shell_sort(sample_arr))


if __name__ == '__main__':
    main()
