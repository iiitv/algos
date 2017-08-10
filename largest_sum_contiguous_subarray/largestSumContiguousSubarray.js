function largestSumContiguousSubarray (arr) {
	/*
	* Find the subarray with maximum sum from all subarrays.
	* :param arr: List of numbers to form subarray from.
	* :return: The maximum sum in all subarrays.
	*/
	let maxPrev = 0;
	let maxNow = 0;
	for (let x = 0; x < arr.length; x++) {
		maxNow += arr[x];
		maxPrev = Math.max(maxPrev, maxNow);
		maxNow = Math.max(0, maxNow);
	}
	return maxPrev;
}

function main () {
	let arr = [-2, -3, 4, -1, -2, 1, 5, -3];
	console.log('Maximum contiguous sum is : ' + largestSumContiguousSubarray(arr));
}

main();
