/*
*  Implementation of heap sort sorting algorithm.
*  Time Complexity: O(N*logN), N being size of array
*  Space Complexity: O(1)
*/

function maxHeapify (arr, size, parent) {
	/*
	*  :param arr: input array.
	*  :param size: hypothetical size of input array.
	*  :param parent: index of current node to create max-heap from.
	*/
	let left = 2 * parent;
	let right = left + 1;
	let largest = parent;  // Initially considering parent as largest
	if (left < size && arr[left] > arr[largest]) {  // Left child is greater than parent
		largest = left;
	}
	if (right < size && arr[right] > arr[largest]) { // Right child is greater than parent
		largest = right;
	}
	if (largest !== parent) {  // If parent is largest then subtree is max-heap
		let temp = arr[parent];
		arr[parent] = arr[largest];  // Swap largest child with parent
		arr[largest] = temp;
		maxHeapify(arr, size, largest);  // Convert upper subtree to max-heap
	}
}

function heapSort (arr) {
	/*
	*  :param arr: Input array to be sorted.
	*/
	for (let i = arr.length / 2 - 1; i >= 0; --i) {  // Build max-heap
		maxHeapify(arr, arr.length, i);
	}

	for (let i = arr.length - 1; i >= 0; --i) {
		let temp = arr[0];  // Swap first and last element
		arr[0] = arr[i];
		arr[i] = temp;
		maxHeapify(arr, i, 0);  // Create Max-Heap on reduced array
	}
}

function main () {
	let arr = [10, -4, 3, 13, 1, 123];
	heapSort(arr);
	console.log(arr);
}

main();
