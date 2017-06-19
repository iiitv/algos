function primeFactor (n) {
	/*
	Finding all the prime factors of given no
	:param n: Number whose prime factors are going to be found
	*/
	for (let i = 2; i <= Math.sqrt(n); i++) {
		if (n % i === 0) {
			console.log(i);
			while ( n % i === 0) {
				n = n / i;
			}
		}
	}
	if (n !== 1) {
		console.log(n)
	}
}

function main () {
	let n = 582;
	console.log('Prime Factors are:');
	for (let i = 2; i <= primeFactor(n); i++) {
		console.log(i);
	}
}

main();
