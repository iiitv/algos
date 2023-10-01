def bubble_sort(arr):
    """
    Performs a bubble sort
    :type arr: int
    """
    for index_1 in range(len(arr)):
        for index_2 in range(0,len(arr)-index_1-1):
            if(arr[index_2]>arr[index_2+1]):
                temp=arr[index_2+1]
                arr[index_2+1]=arr[index_2]
                arr[index_2]=temp


def main():
    arr = [2, 3, 0, 4,-4,56,12]
    print("Before Sorting")
    bubble_sort(arr)
    print(arr)

    
if __name__ == '__main__':
    main()
