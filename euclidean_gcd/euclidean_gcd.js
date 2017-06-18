function euclideanGcdRecursive(first, second) {
	if(second === 0) {
		return first;
	} else {
		return euclideanGcdRecursive(second, (first % second));
	}
}

function euclideanGcd(first, second) {
	while(second !== 0) {
		let temp = second;
		second = first % second;
		first = temp;
	}
	return first;
}

function main() {
	let first = 20;
	let second = 30;
	console.log('Recursive GCD for %d and %d is %d', first, second ,euclideanGcdRecursive(first, second));
	console.log('Iterative GCD for %d and %d is %d', first, second, euclideanGcd(first, second));
}

main();
