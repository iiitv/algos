//  Implementation of dp problem: Longest Palindromic substring

#include <iostream>
#include <string>
#include <vector>

using namespace std;

/*
	Returns the longest substring which is a pallindrome

	@param test input string whose substrings are to be checked
	@return longest substring of input string which is a pallindrome

	Time complexity: O(n^2)
	Space complexity: O(n^2)
	n is size of input string
*/

string longest_palindromic_substring(string test) {
	int n = test.length();
	vector< vector<bool> > substrings(n, vector<bool>(n, false));
	int len_palindrome = 1;
	int palindrome_begin = 0;

	// Substrings of length 1
	for (int i = 0; i < n; ++i) {
		substrings[i][i] = true;
	}

	// Substrings of length 2
	for (int i = 0; i < n - 1; ++i) {
		if (test[i] == test[i + 1]) {
			substrings[i][i + 1] = true;
			palindrome_begin = i;
			len_palindrome = 2;
		}
	}

	// Substrings of length > 3
	for (int i = 3; i <= n; ++i) {
		for (int j = 0; j < n - i + 1; ++j) {
			int tmp = i + j - 1;
			if (substrings[j + 1][tmp - 1] && test[j] == test[tmp]) {
				substrings[j][tmp] = true;
				if (i > len_palindrome) {
					len_palindrome = i;
					palindrome_begin = j;
				}
			}
		}
	}
	return test.substr(palindrome_begin, len_palindrome);
}

int main() {
	string test = "geeksforgeeks";
	cout << "Longest palindromic substring is: " << longest_palindromic_substring(test) << endl;
	return 0;
}

