public class LongestCommonSubsequence {
    //Function that returns Longest Common Subsequence of two strings
    //Time Complexity - O( len(str1) * len(str2) )
    //Space Complexity - O( len(str1)*len(str2) )
    private static String longestCommonSubsequence(String str1, String str2) {
        int[][] arr = new int[str1.length() + 1][str2.length() + 1];
        for (int i = str1.length() - 1; i >= 0; i--) {
            for (int j = str2.length() - 1; j >= 0; j--) {
                if (str1.charAt(i) == str2.charAt(j)) {
                    arr[i][j] = arr[i + 1][j + 1] + 1;
                }
                else {
                    arr[i][j] = Math.max(arr[i + 1][j], arr[i][j + 1]);
                }
            }
        }
        String res = "";
        int i = 0;
        int j = 0;
        while (i < str1.length() && j < str2.length()) {
            if (str1.charAt(i) == str2.charAt(j)) {
                res = res + str1.charAt(i);
                i++;
                j++;
            }
            else if (arr[i + 1][j] >= arr[i][j + 1]) {
                i++;
            }
            else {
                j++;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        String s1 = "applebanana";
        String s2 = "alphabet";
        System.out.println(longestCommonSubsequence(s1, s2));
    }
}
