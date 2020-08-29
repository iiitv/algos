// The edit distance between two strings is the minimum number of operations (insertions, deletions, and
// substitutions of symbols) to transform one string into another. It is a measure of similarity of two strings.
// Edit distance has applications, for example, in computational biology, natural language processing, and spell checking
//This is implementation of Dynamic Programming Algorithm of the popular edit Distance Algorithm in C++
#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;

//this a function that finds the minimum of three integers
ll min (ll a,ll b,ll c)
{
    return min(min(a,b),c);
}

//this is the function that finds the minimum edit distance between two strings string1 and string2.
ll editDistance(string string1,string string2)
{
    ll m = string1.length();//m is the length of string string1
    ll n = string2.length();//n is the length of string string2
    ll dp[m+1][n+1];//this is our two dimensional array where we start from dp[0,0] and go on filling till the
                    // last element based on the values of previously calculated elements.  
                    //the last element i.e. dp[m][n] will be the minimum distance between the two strings

    for (int i = 0; i <= m; i++) 
    { 
        for (int j = 0; j <= n; j++) 
        { 
            //In case the first string is empty, we insert all the characters of the second string
            if (i == 0) 
                dp[i][j] = j;// Min. operations = j 

            //In case the second string is empty, we remove all the characters of the second string
            else if (j == 0) 
                dp[i][j] = i; // Min. operations = i 

            //If the last characters are same, then we ignore them and
            //recur for the remaining string.
            else if (string1[i - 1] == string2[j - 1]) 
                dp[i][j] = dp[i - 1][j - 1]; 

            // If the last characters are different, then we consider all 
            // possibilities - insertion , deletion and substitution
            //and then find the minimum 
            else
                dp[i][j] = 1 + min(dp[i][j - 1],/*insertion*/
                                    dp[i - 1][j],/*deletion*/
                                    dp[i - 1][j - 1]);/*substitution*/ 
        } 
    } 
  
    return dp[m][n];//this is the required minimum edit distance between the two strings. 
    
}

main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string s1,s2;
    cin>>s1>>s2;
    ll d = editDistance(s1,s2);//we obtain the minimum distance using the function editDistance()
    cout<<d<<endl;
}