#include <stdio.h>
#include <string.h>

#define max(a,b) (a > b) ? a : b

// Function that computes the longest common subsequence
// Complexity: O( len(string1) * len(string2) )
int longestCommonSubsequence(char *string1, char *string2) {
	int len1 = (int) strlen(string1);
	int len2 = (int) strlen(string2);
	int lcs[len1 + 1][len2 + 1];

	for (int i = 0; i <= len1; ++i) {
		for (int j = 0; j <= len2; ++j) {
			if (i == 0 || j == 0) {
				lcs[i][j] = 0;
			} else if (string1[i - 1] == string2[j - 1]) {
				lcs[i][j] = lcs[i - 1][j - 1] + 1;
			} else {
				lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1]);
			}
		}
	}

	return lcs[len1][len2];
}


int main() {
	// String from which Longest common subsequence have to find
	// Maximum length of string should be 100 char long
	char str1[100];
	char str2[100];
	strcpy(str1, "mathematicians study maths");
	strcpy(str2, "people study matrix multiplication");
	printf("%d\n", longestCommonSubsequence(str1, str2));
	return 0;
}
