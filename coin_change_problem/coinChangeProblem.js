function coinChangeProblem (coins, amount) {
	/*
	* Find out maximum number of ways in which a amount can
	* be obtained using fixed value coins.
	* Time Complexity : O((type of coins)*amount)
	* :param coins: Iterable of elements containing value of coins.
	* :param amount: It is value which is to be obtained with coins.
	* :return: returns maximum number of ways amount can be arranged in.
	*/
	let possibilities = new Array(amount + 1);
	possibilities.fill(0);
	possibilities[0] = 1;
	for (let i = 0; i < coins.length; i++) {
		for (let j = coins[i]; j <= amount; j++) {
			possibilities[j] += possibilities[j - coins[i]];
		}
	}
	return possibilities[amount];
}

function main () {
	let coins = [1, 2, 3];
	let amount = 10;
	console.log(coinChangeProblem(coins, amount));
}

main();
