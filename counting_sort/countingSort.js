/* Following algorithm sorts the input array in ascending order
*  Time complexity is O(n+k)
*  Auxiliary space is O(n+k)
*  n is number of elements and k is the range of input
*  max is the maximum element in array
*/

function countingSort (arr, max) {
	/*
	:param arr: Array to be sorted
	:param max: Maximum value in array
	:return: Sorted array
	*/
	let n = arr.length;
	let count = new Array(max + 1);
	let temp = new Array(n);
	count.fill(0);
	for (let i = 0; i < n; i++) {
		count[arr[i]]++;
	}
	for (let i = 1; i <= max; i++) {
		count[i] += count[i - 1];
	}
	for (let i = 0; i < n; ++i) {
		temp[count[arr[i]] - 1] = arr[i];
		count[arr[i]]--;
	}
	return temp;
}

function main () {
	let max = 10;
	let arr = [3, 7, 10, 3, 1, 9, 4, 9];
	arr = countingSort(arr, max);
	console.log(arr);
}

main();
