function euclidean_gcd_recursive(first, second) {
	if(second === 0) {
		return first;
	} else {
		return euclidean_gcd_recursive(second, (first % second));
	}
}

function euclidean_gcd(first, second) {
	while(second != 0) {
		let temp = second;
		second = first % second;
		first = temp;
	}
	return first;
}

function main() {
	let first = 20;
	let second = 30;
	console.log('Recursive GCD for %d and %d is %d', first, second ,euclidean_gcd_recursive(first, second));
	console.log('Iterative GCD for %d and %d is %d', first, second, euclidean_gcd(first, second));
}

main();
