/*
 *  Following implementation of Soundex algo used to phonetic codes
 *  Phonetic codes shows the identification of simillar words
 */


public class SoundexCode
{
	public static void main(String[] args)
	{
		String word1 = "meet";
		String word2 = "meat";
		String word3 = "meetpaija";
		String word4 = "met";
		
		// EXPECTED : Soundex code for word1, word2 and word4 should be same 
		
		System.out.println(fetchCode(word1));
		System.out.println(fetchCode(word2));
		System.out.println(fetchCode(word3));
		System.out.println(fetchCode(word4));
	}
	
    public static String fetchCode(String word)
    {
        char[] chars = word.toUpperCase().toCharArray();
        char firstChar = chars[0];
 
        //fetch code
        for (int i = 0; i < chars.length; i++) {
            switch (chars[i]) {
            case 'B':
            case 'F':
            case 'P':
            case 'V': {
                chars[i] = '1';
                break;
            }
 
            case 'C':
            case 'G':
            case 'J':
            case 'K':
            case 'Q':
            case 'S':
            case 'X':
            case 'Z': {
                chars[i] = '2';
                break;
            }
 
            case 'D':
            case 'T': {
                chars[i] = '3';
                break;
            }
 
            case 'L': {
                chars[i] = '4';
                break;
            }
 
            case 'M':
            case 'N': {
                chars[i] = '5';
                break;
            }
 
            case 'R': {
                chars[i] = '6';
                break;
            }
 
            default: {
                chars[i] = '0';
                break;
            }
            }
        }
 
        //Remove duplicates
        String outputCode = "" + firstChar;
         
        for (int i = 1; i < chars.length; i++)
            if (chars[i] != chars[i - 1] && chars[i] != '0')
                outputCode += chars[i];
 
        //Pad with 0's or truncate
        outputCode = outputCode + "0000";
        return outputCode.substring(0, 4);
    }
    
}