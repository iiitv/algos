function expandAroundCenter (test, left, right) {
	let n  = test.length;
	while (left >= 0 && right < n  && test.charAt(left) === test.charAt(right)) {
		left--;
		right++;
	}
	return right - left - 1;
}

function longestPalindromicSubstring (test) {
	let start = 0;
	let end = 0;

	for (let i = 0; i < test.length; i++) {
		let length = Math.max(expandAroundCenter(test, i, i), expandAroundCenter(test, i, i + 1));
		if (length > end - start) {
			start = i - Math.floor((length - 1) / 2);
			end = i + Math.floor(length / 2);
		}
	}
	return test.slice(start, end + 1);
}

function main () {
	let test = 'geeksforgeeks';
	console.log('Longest Palindromic Substring of', test, 'is', longestPalindromicSubstring(test));
}

main();