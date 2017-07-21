/*
*	Implementation of merge sort algorithm
*	Time complexity: O(size*log(size))
*	Space complexity: O(size)
*/
function merge (left, right) {
	let i = 0;
	let j = 0;
	let size = left.length + right.length;
	let arr = [];
	for (let k = 0; k < size; k++) {
		if (i > left.length - 1 && j < right.length) {
			arr[k] = right[j];
			j++;
		} else if (j > right.length - 1 && i < left.length) {
			arr[k] = left[i];
			i++;
		} else if (left[i] < right[j]) {
			arr[k] = left[i];
			i++;
		} else {
			arr[k] = right[j];
			j++;
		}
	}
	return arr;
}

/*
*	:param arr: array to be sorted
*/
function mergeSort (arr) {
	if (arr.length < 2) {
		return arr;
	}
	let middle = parseInt(arr.length / 2);
	let left = arr.slice(0, middle);
	let right = arr.slice(middle, arr.length);
	return merge(mergeSort(left), mergeSort(right));
}

function main () {
	let arr = [2, 1, 6, 444, 8, 99, 10];
	console.log('Sorted data is :');
	arr = mergeSort(arr);
	console.log(arr);
}

main();
