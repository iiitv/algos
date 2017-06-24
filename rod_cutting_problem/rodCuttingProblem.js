/*
* Problem Statement: Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n.
* Determine the maximum value obtainable by cutting up the rod and selling the pieces.
*/

function rodCuttingProblem (price) {
	/*
	Computes maximum money that can be earned by cutting a rod of length n (Bottom-Up Approach).
    Time Complexity : O(n^2)
    Space Complexity : O(n)
    :param price: List in which price[i] denotes price of rod of length i.
    :return: returns optimal solution for rod of length n.
	*/
	let n = price.length;
	let best_price = new Array(n + 1);
	best_price.fill(0);
	for (let i = 1; i < best_price.length; i++) {
		best_price[i] = price[i-1];
	}
	console.log(best_price);
	for (let i = 1; i <= n; i++) {
		for (let j = i; j <= n+1; j++) {
			best_price[j] = Math.max(best_price[j], best_price[j-i] + best_price[i]);
		}
	}
	return best_price[n];
}

function main () {
	let price = [10, 52, 84, 93, 101, 17, 117, 20];
	console.log('Maximum obtainable value is : ' + rodCuttingProblem(price));
}

 main();
