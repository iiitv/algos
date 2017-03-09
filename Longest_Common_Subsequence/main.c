/*
 * Author: Yash Ladha
 * Topic : Longest Common Subsequence
 * Domain: Dynamic Programming
 */

#include <stdio.h>
#include <string.h>

void longestCommonSubsequence(char *string1, char *string2);

int max(int x, int y);

int main() {
    // String from which Longest common subsequence have to find
    // Maximum length of string should be 100 char long
    char str1[100];
    char str2[100];
    scanf("%s", str1);
    scanf("%s", str2);
    longestCommonSubsequence(str1, str2);
    return 0;
}

// Function that computes the longest common subsequence
// Complexity: O( len(string1) * len(string2) )
void longestCommonSubsequence(char *string1, char *string2) {
    int len1 = (int) strlen(string1);
    int len2 = (int) strlen(string2);
    int lcs[len1 + 1][len2 + 1];

    for (int i = 0; i <= len1; ++i) {
        for (int j = 0; j <= len2; ++j) {
            if (i == 0 || j == 0)
                lcs[i][j] = 0;
            else if (string1[i - 1] == string2[j - 1])
                lcs[i][j] = lcs[i - 1][j - 1] + 1;
            else
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1]);
        }
    }

    printf("%d\n", lcs[len1][len2]);
    return;
}

int max(int x, int y) {
    return (x > y) ? x : y;
}
