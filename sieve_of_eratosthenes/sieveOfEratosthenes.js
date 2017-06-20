function sieveOfEratosthenes (n) {
	/*
    * Calculates prime numbers till a number n
    * :param n: Number upto which to calculate primes
    * :return: A boolean list contaning only primes
    */
    primes = new Array(n + 1);  // set all as true initially
    primes.fill(true);
    primes[0] = primes[1] = false;  //Handling case for 0 and 1
    sqrt_n = Math.ceil(Math.sqrt(n));
    for (let i = 2; i <= sqrt_n; i++)
        if (primes[i])
            for (let j = 2*i; j <= n; j+=i)
                primes[j] = false;
    return primes;
}

function main () {
	let n = 319; // number till where we wish to find primes
	primes = sieveOfEratosthenes(n);
	for (let i = 1; i <= n; i++)
        if (primes[i])
            console.log(i);
}

main();
