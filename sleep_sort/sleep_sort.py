"""
Sleep sort is a proof of concept sorting algorithm that creates threads for
each number in the sorting queue and sleeps for the amount of time before
giving the result.

It has no practical usage and doesn't works for negative numbers. Also for
very close positive numbers, results are not guaranteed to be consistent.
"""
try:
    import queue
except ImportError:
    import Queue as queue
import threading
import time


def sleeper(number, sorted_numbers):
    """
    Worker function for sleep sort's thread.
    :param number: Number for the thread
    :param sorted_numbers: Queue which contains the sorted numbers
    """
    time.sleep(number)
    sorted_numbers.put(number)


def sleep_sort(numbers, reverse=False):
    """
    Sorts the numbers using sleep sort algorithm.
    :param numbers: Iterable object containing numbers
    :param reverse: Whether results need to be reverse
    :returns: A generator with sorted numbers
    """
    threads = []
    sorted_numbers = queue.LifoQueue() if reverse else queue.Queue()
    for number in numbers:
        thread = threading.Thread(target=sleeper,
                                  args=(number, sorted_numbers))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    while not sorted_numbers.empty():
        yield sorted_numbers.get()


def main():
    numbers = [2, 3, 4, 1]
    print("Ascending order: ")
    for number in sleep_sort(numbers):
        print(number)
    print("Descending order: ")
    for number in sleep_sort(numbers, reverse=True):
        print(number)


if __name__ == '__main__':
    main()
