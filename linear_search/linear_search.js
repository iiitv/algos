function linearSearch (arr, x) {
	/*
	Performs a linear search
	:param arr: List of elements to search from
	:param x: Element to search for
	:return: Index if element found else -1
	*/
	for (let it = 0; it < arr.length; it++) {
		if (arr[it] === x) {
			return it;
		}
	}
	return -1;
}

function main () {
	let A = [];
	for (let i = 1; i<=100; i++) {
		A.push(i);
	}
	let index = linearSearch(A, 12);
	if (index === -1) {
		console.log('Element was not found');
	} else {
		console.log('Element was found at %dth index', index);
	}
}

main();
