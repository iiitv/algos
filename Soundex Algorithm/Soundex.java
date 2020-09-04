package soundex;

import java.util.Scanner;

public class Soundex {

	public static String soundex(String str) {

		char[] s = str.toUpperCase().toCharArray();
		//retaining first letter
		String output = s[0] + "";

		//replacing consonants with digits
		for(int i = 0; i<s.length; i++) {
			switch(s[i]) {
				case 'B':
				case 'F':
				case 'P':
				case 'V':
					s[i] = '1';
					break;

				case 'C':
				case 'G':
				case 'J':
				case 'K':
				case 'Q':
				case 'S':
				case 'X':
				case 'Z':
					s[i] = '2';
					break;
				
				case 'D':
				case 'T':
					s[i] = '3';
					break;

				case 'L':
					s[i] = '4';
					break;

				case 'M':
				case 'N':
					s[i] = '5';
					break;

				case 'R':
					s[i] = '6';
					break;

				default:
					s[i] = '0';
					break;

			}
		}

		// removing duplicates
		for(int i = 1; i < s.length; i++) {
			if(s[i] != s[i-1] && s[i] != '0')
				output += s[i];
		}

		// right padding with zeroes or truncating
		output = output + "0000";
		return output.substring(0, 4);
	}

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the string");
		String str = sc.nextLine();
		String str_output = soundex(str);
		System.out.println(str_output);
	}
}