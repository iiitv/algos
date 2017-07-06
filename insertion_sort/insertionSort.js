/* Following algorithm sorts the input array in ascending order
* Time Complexity : O(n^2)
* Auxiliary Space: O(1)
* n is the number of elements in the array to be sorted
*/

function insertionSort (arr) {
	/*
	: param arr : Array to be sorted
	: return : Sorted Array
	*/
	for (let i = 1; i < arr.length; i++) {
		let j = i - 1;
		let temp = arr[i];
		while (j >= 0 && arr[j] > temp) {
			arr[j + 1] = arr[j];
			j--;
		}
		arr[j + 1] = temp;
	}
	return arr;
}

function main () {
	let arr = [5, 9, 3, 1, 99];
	arr = insertionSort(arr);
	console.log(arr);
}

main();
