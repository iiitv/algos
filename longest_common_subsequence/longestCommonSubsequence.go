package main

import (
	"fmt"
	"math"
)

// Time complexity : O(len(str1)*len(str2))
// longestCommonSubsequence returns length of the LCS
func longestCommonSubsequence(str1, str2 string) int {
	len1 := len(str1)
	len2 := len(str2)
	lcs := make([][]int, len1+1)
	for i := range lcs {
		lcs[i] = make([]int, len2+1)
	}
	for i := 0; i <= len1; i++ {
		for j := 0; j <= len2; j++ {
			if i == 0 || j == 0 {
				lcs[i][j] = 0
			} else if str1[i-1] == str2[j-1] {
				lcs[i][j] = lcs[i-1][j-1] + 1
			} else {
				lcs[i][j] = int(math.Max(float64(lcs[i-1][j]), float64(lcs[i][j-1])))
			}
		}
	}
	return lcs[len1][len2]
}

// Driver function to test above algorithm
func main() {
	str1 := "mohit"
	str2 := "mokyit"
	fmt.Println(longestCommonSubsequence(str1, str2))
}
