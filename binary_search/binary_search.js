function binarySearchIterative (arr, item) {
	/*
	Performs a binary search iteratively
	:param arr: List of elements to search from
	:param item: Element to search for
	:return: returns index if element found else -1
	 */
	let begin = 0;
	let end = arr.length - 1;
	while (begin <= end) {
		let mid = Math.floor((begin + end) / 2);
		if (arr[mid] === item) {
			return mid;
		} else if (arr[mid] > item) {
			end = mid - 1;
		} else {
			begin = mid + 1;
		}
	}
	return -1;
}

function binarySearchRecursive (arr, item, begin, end) {
	/*
	Performs a binary search recursively
	:param arr: List of elements to search from
	:param item: Element to search for
	:param begin: Left limit of array
	:param end: Right limit of array
	:return: returns index if element found else -1
	 */
	if (begin <= end) {
		let mid = Math.floor((begin + end) / 2);
		if (arr[mid] === item) {
			return mid;
		} else if (arr[mid] > item) {
			return binarySearchRecursive(arr, item, begin, mid - 1);
		} else {
			return binarySearchRecursive(arr, item, mid + 1, end);
		}
	} else {
		return -1;
	}
}

function main () {
	let arr = [2, 5, 6, 7, 8, 9, 10];
	let item = 5;
	if (binarySearchIterative(arr, item) === -1) {
		console.log('Element is not found');
	} else {
		console.log('Element is found');
	}

	if (binarySearchRecursive(arr, item, 0, arr.length - 1) === -1) {
		console.log('Element is not found');
	} else {
		console.log('Element is found');
	}
}

main();
