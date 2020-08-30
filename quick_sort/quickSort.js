/*
*	Implementation of quicksort algorithm
*	Time complexity: O(nlogn)
* 	Space complexity: O(n)
*	n is the size of array
*/
function median (arr, i, j, k) {
	/*
	:param arr: array of elements
	:param i: index of first element
	:param j: index of last element
	:param k: index of middle element
	:return: return median of values at indices i, j and k
	*/
	if (arr[i] > arr[j] && arr[i] > arr[k]) {
		if (arr[k] > arr[j]) {
			return k;
		} else {
			return j;
		}
	} else if (arr[j] > arr[i] && arr[j] > arr[k]) {
		if (arr[k] > arr[i]) {
			return k;
		} else {
			return i;
		}
	} else {
		if (arr[i] > arr[j]) {
			return i;
		} else {
			return j;
		}
	}
}

function partition (arr, start, end) {
	/*
	:param arr: array of elements
	:param start: index of first element
	:param end: index of last element
	:return: return value for function, used in partitioning of array
	*/
	let j = start - 1;
	let tmp;
	let pi = median(arr, start, end, parseInt((start + end) / 2));
	tmp = arr[pi];
	arr[pi] = arr[end];
	arr[end] = tmp;
	let pivot = arr[end];
	for (let i = start; i < end; i++) {
		if (arr[i] <= pivot) {
			j++;
			tmp = arr[i];
			arr[i] = arr[j];
			arr[j] = tmp;
		}
	}
	tmp = arr[j + 1];
	arr[j + 1] = arr[end];
	arr[end] = tmp;
	return j + 1;
}

function quickSort (arr, left = 0, right = arr.length - 1) {
	/*
	:param arr: array to be sorted
	:param left: index of first element
	:param right: index of last element
	*/
	if (left < right) {
		let p = partition(arr, left, right);
		quickSort(arr, left, p - 1);
		quickSort(arr, p + 1, right);
	}
}

function main () {
	let arr = [2, 1, 6, 44, 8, 9, 10];
	quickSort(arr);
	console.log('Sorted data is', arr);
}

main();
