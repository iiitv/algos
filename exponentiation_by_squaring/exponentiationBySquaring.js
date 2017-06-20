function exponentiationBySquaring (base, power) {
	/*
	Performs Exponentiation By Squaring.
	:param base: Base of expression.
	:param power: Power of expression.
	:return: Returns (base ^ power).
	*/
	if (power < 0) { // When Power is Negative
		return exponentiationBySquaring(1 / base, -power);
	} else if (power === 0) { // Power = 0 (Base Case 1)
		return 1;
	} else if (power === 1) { // Power = 1 (Base Case 2)
		return base;
	} else if (power % 2 === 0) { // When Power is Even
		return exponentiationBySquaring(base * base, power >> 1);
	} else { // When Power is Odd
		return base * exponentiationBySquaring(base * base, (power - 1) >> 1);
	}
}

function main () {
	let base = 3;
	let power = 6;
	let res = exponentiationBySquaring(base, power);
	console.log('%d\n', res);
}

main();
