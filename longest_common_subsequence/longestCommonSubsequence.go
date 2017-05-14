package main

import (
	"fmt"
	"math"
)

// longestCommonSubsequence driver function
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

func main() {
	var str1, str2 string
	fmt.Scanln(&str1)
	fmt.Scanln(&str2)
	fmt.Println(longestCommonSubsequence(str1, str2))
}
