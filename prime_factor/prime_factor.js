function primeFactor (n) {
	/*
	Finding all the prime factors of a given number
	:param n: Number whose prime factors are going to be found
	:returns: Array with prime numbers
	 */
	let primes = [];
	for (let i = 2; i <= Math.sqrt(n); i++) {
		if (n % i === 0) {
			primes.push(i);
			while (n % i === 0) {
				n = n / i;
			}
		}
	}
	if (n !== 1) {
		primes.push(n);
	}
	return primes;
}

function main () {
	let n = 582;
	console.log('Prime factors are:');
	let primes = primeFactor(n);
	for (let i = 0; i < primes.length; i++) {
		console.log(primes[i]);
	}
}

main();
