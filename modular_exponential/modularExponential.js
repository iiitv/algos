function modularExponential (base, power, mod) {
	/*
	Performs Modular Exponential.
	Time Complexity : O(log (power))
	:param base: Number that is going to be raised.
	:param power: Power to which the number is raised.
	:param mod: Number by which modulo has to be performed.
	:return: Returns (base ^ power) % mod
	*/
	let answer = 1;
	base = base % mod;
	while (power) {
		if (power & 1) {
			answer = (answer * base) % mod;
		}
		power = power >> 1;
		base = (base * base) % mod;
	}
	return answer;
}

function main () {
	let base = 3;
	let power = 5;
	let mod = 61;
	let res = modularExponential(base, power, mod);
	console.log('%d\n', res);
}

main();
