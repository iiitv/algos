package main

import "fmt"

// expandAroundCenter returns length of palindromic substring
func expandAroundCenter(runes []rune, left int, right int) int {
	n := len(runes)

	for left >= 0 && right < n && runes[left] == runes[right] {
		left--
		right++
	}
	return right - left - 1
}

// LongestPalindromicSubstring returns the longest palindromic substring in
// provided string.
// Time complexity: O(n^2)
// Space complexity: O(1)
func LongestPalindromicSubstring(str string) string {
	start, end := 0, 0
	runes := []rune(str)

	for i := 0; i < len(runes); i++ {
		a := expandAroundCenter(runes, i, i)
		b := expandAroundCenter(runes, i, i+1)

		length := 0
		if a > b {
			length = a
		} else {
			length = b
		}

		if length > end-start {
			start = i - (length-1)/2
			end = i + length/2
		}
	}
	return string(runes[start : end+1])
}

func main() {
	str := "And the longest palindrome is... neveroddoreven!"
	fmt.Println(LongestPalindromicSubstring(str))
}
