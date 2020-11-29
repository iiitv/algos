/**
 * <p>This class represents a Min Heap to be used for doing a heap sort.</p>
 *
 * <p>A min heap is a perfectly balanced binary tree with the invariant that a parent is always less than any of its children.
 * There's no guaranteed relationship between siblings.</p>
 *
 * <p>On the constructor the elements to be sorted will be copied and the min heap will be created. This step takes time O(n log n)
 * Then calling {@link this#min} will remove and returns the min element in O(log n) time. Using this class heap sort
 * will take total time of O(n log n)</p>
 *
 * <p>This implementation uses an array. Because a Heap is guaranteed to be perfectly balanced, you can store the root of the heap
 * as element 0, then left and right children on indexes 1 and 2, then children for the left child of the root on indexes 3 and 4
 * and so on. That means that going from a parent to one of its children or vice versa takes O(1) time.</p>
 *
 * <p>This class doesn't represent a fully featured Min Heap class, it has been optimized to be used for heap sort, but implementing
 * a feature-complete class shouldn't be easy to adapt from this.</p>
 */
class MinHeap {

    private int[] elements;
    private int size;

    /**
     * Creates a Min Heap for the given elements.
     *
     * @param elements
     */
    public MinHeap(final int[] elements) {
        this.size = 0;
        this.elements = new int[elements.length];
        for (int i = 0; i < elements.length; ++i) {
            this.elements[i] = elements[i];
            heapify();
            ++size;
        }
    }

    /**
     * <p>Given the index of an element, returns the index of its parent.</p>
     *
     * <p>If the element doesn't have a parent, returned index will be less than 0</p>
     *
     * @param index
     * @return
     */
    private int parentIndex(final int index) {
        return (index - 1) / 2;
    }

    /**
     * <p>Given the index of an element, returns the index of its left child.</p>
     *
     * <p>If the element doesn't have a left child, returned index will be greater than size.</p>
     *
     * @param index
     * @return
     */
    private int leftChildIndex(final int index) {
        return 2 * index + 1;
    }

    /**
     * <p>Given the index of an element, returns the index of its right child, which is always 1 more
     * than the index returned by {@link this#leftChildIndex(int)}.</p>
     *
     * <p>If the element doesn't have a right child, returned index will be greater than size.</p>
     *
     * @param index
     * @return
     */
    private int rightChildIndex(final int index) {
        return leftChildIndex(index) + 1;
    }

    /**
     * <p>Makes the backing array of this object, a heap.</p>
     *
     * <p>This method needs to be called after a new element has been added, to work.</p>
     *
     * <p>It'll look at the newly added element and check its parent. If it's lesser then elements will be swapped
     * to maintain the min heap's invariant. This operation will be done recursively until there's no more need to
     * swap elements or the root is reached</p>
     */
    private void heapify() {
        int index = size;
        while (parentIndex(index) >= 0 && elements[parentIndex(index)] > elements[index]) {
            swap(parentIndex(index), index);
            index = parentIndex(index);
        }
    }

    /**
     * Swap elements at the given positions
     *
     * @param i
     * @param j
     */
    private void swap(int i, int j) {
        int temp = elements[i];
        elements[i] = elements[j];
        elements[j] = temp;
    }

    /**
     * <p>Returns and retrieves the min element of the min-heap</p>
     *
     * <p>After the element is retrieved, the heap's invariant is probably broken so {@link this#makeHeap} is
     * called to restore it.</p>
     *
     * @return
     */
    public int min() {
        int min = elements[0];
        --size;
        makeHeap();
        return min;
    }

    /**
     * <p>After the min-element is returned, this method will restore the min-heap's invariant.</p>
     *
     * <p>First it'll put the last element in the, now empty, root. Then it will check if that element is not less
     * than its both children. If that's not the case, it will be swapped with the lesser and the process will be
     * repeated recursively until a swap is not needed or it reaches a leaf element.</p>
     */
    private void makeHeap() {
        swap(0, size);
        int index = 0;
        while (leftChildIndex(index) < size) {
            int minChildIndex = leftChildIndex(index);
            if (rightChildIndex(index) < size && elements[rightChildIndex(index)] < elements[minChildIndex]) {
                minChildIndex = rightChildIndex(index);
            }
            if (elements[parentIndex(index)] < elements[minChildIndex]) {
                return;
            }
            swap(parentIndex(index), minChildIndex);
            index = minChildIndex;
        }
    }
}

public class HeapSort {

    public static void heapSort(int[] elements) {
        MinHeap heap = new MinHeap(elements);
        for (int i = 0; i < elements.length; ++i) {
            elements[i] = heap.min();
        }
    }

    public static void main(String[] args) {
        int[] elements = new int[] {10, 4, 3, 13, 1, 123};  // Creating Test array

        heapSort(elements);  // Sort the array
        for (int element : elements) { // Printing sorted array
            System.out.print(element + " ");
        }
    }
}
