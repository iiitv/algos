/*
* Problem Statement: Given a rod of length n and an array of prices that contains prices of all pieces of size smaller than n.
* Determine the maximum value obtainable by cutting up the rod and selling the pieces.
*/

function rodCuttingProblem (price) {
	/*
	Computes maximum money that can be earned by cutting a rod of length n (Bottom-Up Approach).
	Time Complexity	:	O(n ^ 2)
	Space Complexity : O(n)
	:param price:	Array in which price[i] denotes price	of rod of length i.
	:return: returns maximum value obtainable by cutting up the rod and selling the pieces.
	*/
	let n = price.length;
	let bestPrice = new Array(n + 1);
	bestPrice.fill(0);
	for (let i = 1; i < bestPrice.length; i++) {
		bestPrice[i] = price[i - 1];
	}
	for (let i = 1; i <= n; i++) {
		let tmax = Number.MIN_SAFE_INTEGER;
		for (let j = 0; j < i; j++) {
			tmax = Math.max(tmax, bestPrice[i - j - 1] + price[j]);
		}
		bestPrice[i] = tmax;
	}
	return bestPrice[n];
}

function main () {
	let price = [10, 52, 84, 93, 101, 17, 117, 20];
	console.log('Maximum obtainable value is : ' + rodCuttingProblem(price));
}

main();
