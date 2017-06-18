/*
 * Worst case time complexity = O(n^2)
 * Best case complexity = O(nlog(n))
 * returns sorted data
 */
function shellSort (data) {
	for (let i = Math.floor(data.length/2); i > 0; i = Math.floor(i/2)) {
		for (let j = i; j < data.length; j++) {
			for (let k = j - i; k >= 0; k -= i) {
				if (data[k+i] >= data[k]) {
					break;
				} else {
					var temp = data[k];
					data[k] = data[k+i];
					data[k+i] = temp;
				}
			}
		}
	}
	return data;
}

function main () {
	let data = [1000, 45, -45, 121, 47, 45, 65, 121, -1, 103, 45, 34];
	console.log(shellSort(data));
}

main();
