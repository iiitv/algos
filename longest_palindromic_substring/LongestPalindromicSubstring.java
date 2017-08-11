public class LongestPalindromicSubstring {

    /*
    This method is used to determine palindrome about a point in string.
    @param test: Input string whose substrings are to be checked
    @param left: Left end of result palindromic substring
    @param right: Right end of result palindromic substring
    @return: Length of palindromic substring
    */
    private static int expandAroundCenter(String test, int left, int right) {
        int lengthOfString = test.length();
        while (left >= 0 && right < lengthOfString && test.charAt(left) == test.charAt(right)) {
            left -= 1;
            right += 1;
        }
        return right - left - 1;
    }

    /*
    Method to find longest substring which is a palindrome.
    @param test: Input string whose substrings are to be checked
    @return: Longest substring of input string which is a palindrome

    Time complexity: O(lengthOfString^2)
    Space complexity: O(1)
    */
    public static String longestPalindromicSubstring(String test) {
        String toTest = test.toLowerCase();
        int start = 0;
        int end = 0;
        int lengthOfString = test.length();
        for (int i = 0; i < lengthOfString; ++i) {
            int length = Math.max(expandAroundCenter(toTest, i, i), expandAroundCenter(toTest, i, i + 1));
            if (length > end - start) {
                start = i - (length - 1) / 2;
                end = i + length / 2;
            }
        }
        return test.substring(start, end + 1);
    }

    public static void main(String[] args) {
        String test = "Nitin";
        System.out.println("Longest Palindromic Substring of " +
                            test + " is " +
                            longestPalindromicSubstring(test));
    }
}
