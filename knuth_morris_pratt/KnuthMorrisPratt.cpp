#include <iostream>
using namespace std;

int * generate_pattern_array ( string pattern ) {
    
    int i, j=0;
    int len = pattern.length();
    int * ar = new int[len];
    
    for ( i=1 ; i<len; ++i ) {
        
        if ( pattern[i] == pattern[j] ) {
            ar[i] = j+1;
            j++;
        }
        else {
            if ( j != 0 ) {
                j = ar[j-1];
                i--;
            }
            else 
                ar[i] = 0;
        }
    }
    return ar;
}

bool KMP ( string text, string pattern ) {
    
    int * ar = generate_pattern_array ( pattern );
    int i, j=0, text_len=text.length(), pattern_len = pattern.length();
    
    for ( i=0; i < text_len && j < pattern_len ; ++i ) {
        if ( text[i] == pattern[j] ) {
            j++;
        }
        else {
            if ( j != 0 ) {
                j = ar[j-1];
                i--;
            }
        }
    }
    
    if ( j == pattern_len )
        return true;
    else
        return false;
    
}

int main()
{
    string text = "abcdabcde";
    string pattern = "cdab";
    
    string output = (KMP(text, pattern)==true)?"Substring found":"Substring not found";
    
    cout<<output<<endl;
    
    return 0;
}
