function primeFactor (n) {
	for (let i = 2; i <= n; i++) {
		if (n % i === 0) {
			console.log(i);
			while (n % i === 0) {
				n = n / i;
			}
		}
	}
}

function main () {
	let n = 8;
	console.log('Prime Factors are:');
	for (let i = 2; i <= primeFactor(n); i++) {
		console.log(i);
	}
}

main();
