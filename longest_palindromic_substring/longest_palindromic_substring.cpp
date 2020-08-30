//  Implementation of dp problem: Longest Palindromic substring

#include <iostream>
#include <string>
#include <vector>

using namespace std;
/*
	Returns the length of palindromic substring

	@param test: input string whose substrings are to be checked
	@param left: Left end of result palindromic substring
	@param right: Right end of result palindromic substring
	@return: Length of palindromic substring
*/

int expand_around_center(string test, int left, int right) {
	int n = test.length();

	while (left >= 0 && right < n && test[left] == test[right]) {
		left -= 1;
		right += 1;
	}
	return right - left - 1;
}

/*
	Returns the longest substring which is a pallindrome

	@param test: input string whose substrings are to be checked
	@return longest substring of input string which is a pallindrome

	Time complexity: O(n^2)
	Space complexity: O(1)
	n is size of input string
*/

string longest_palindromic_substring(string test) {
	int start = 0, end = 0;
	int n = test.length();

	for (int i = 0; i < n; ++i) {
		int length = max(expand_around_center(test, i, i), expand_around_center(test, i, i + 1));
		if (length > end - start) {
			start = i - (int)((length - 1) / 2);
			end = i + (int)(length / 2);
		}
	}
	return test.substr(start, end - start + 1);
}

int main() {
	string test = "iiit";
	cout << "Longest palindromic substring is: " << longest_palindromic_substring(test) << endl;
	return 0;
}

