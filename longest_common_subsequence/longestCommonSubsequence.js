function longestCommonSubsequence (str1, str2) {
	/*
	* Time Complexity - O(len(str1) * len(str2))
	* Space Complexity - O(len(str1) * len(str2))
	* :param seq1: First sequence
	* :param seq2: Second sequence
	* :return: The longest common subsequence of two input sequences
	*/
	let len1 = str1.length;
	let len2 = str2.length;
	let lcs = new Array(len1 + 1);
	for (let x = 0; x <= len1; x++) {
		lcs[x] = new Array(len2 + 1);
	}
	for (let i = 0; i <= len1; i++) {
		for (let j = 0; j <= len2; j++) {
			if (i === 0 || j === 0) {
				lcs[i][j] = 0;
			} else if (str1[i - 1] === str2[j - 1]) {
				lcs[i][j] = lcs[i - 1][j - 1] + 1;
			} else {
				lcs[i][j] = Math.max(lcs[i - 1][j], lcs[i][j - 1]);
			}
		}
	}
	let res = '';
	let i = len1;
	let j = len2;
	while (i > 0 && j > 0) {
		if (str1[i - 1] === str2[j - 1]) {
			res = str1[i - 1] + res;
			i--;
			j--;
		} else if (lcs[i - 1][j] > lcs[i][j - 1]) {
			i--;
		} else {
			j--;
		}
	}
	return res;
}

function main () {
	let a = 'whattheheckman';
	let b = 'whatareyoudoinghere';
	console.log('Longest Common Subsequence : ' + longestCommonSubsequence(a, b));
}

main();
