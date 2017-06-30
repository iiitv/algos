function largestSumContiguousSubarray (arr) {
	/*
	* Find the subarray with maximum sum from all subarrays.
	* :param arr: List of numbers to form subarray from.
	* :return: The maximum sum in all subarrays.
	*/
	let max_prev = 0, max_now = 0;
	for(let x = 0; x < arr.length; x++) {
		max_now += arr[x];
		max_prev = Math.max(max_prev, max_now);
		max_now = Math.max(0, max_now);
	}
	return max_prev;
}

function main () {
	let arr = [-2, -3, 4, -1, -2, 1, 5, -3];
	console.log('Maximum contiguous sum is : ' + largestSumContiguousSubarray(arr));
}

main();
