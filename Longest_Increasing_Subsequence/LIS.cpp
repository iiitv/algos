#include <bits/stdc++.h>
using namespace std;

/* Longest Increasing Subsequence Solution in O(nlogn) */

int Long_Inc_Subsqnc(vector<int> sequence)
{
    /*
    Checking whether the sequence is empty or not
    */

    if(sequence.size()==0)
    {
        return 0;
    }

    /*
    Creating another vector that will keep track of the last element of the 
    increasing subsequence of length equal to (index+1) in the vector
    ex track[0]= 10 , means longest increasing subsequence of length 1 ends with 10
    */
    vector<int> track;
    track.push_back(sequence[0]);

    /* initialising the default length of 1 of longest increasing subsequence */
    int length = 1;

    /*traversing the sequence */

    for(int i=1;i<sequence.size();i++)
    {
        /* if current element in our sequence is less than the last element of longest 
        increasing subsequence of length 1 then we will replace it with our current 
        element to have further better chances*/

        if(sequence[i]<track[0])
        {
            track[0] = sequence[i];
        }

        /* if current element in our sequence is greater than the last element of longest 
        increasing subsequence of largest length till now then we will append it to track vector*/

        else if(sequence[i]>track[length-1])
        {
            
            track.push_back(sequence[i]);
            length++;
        }

        /* else through binary searching we will find the appropriate place to replace
        the current element with the last element of longest increasing subsequence of length L
        */

        else{
            int first = 0;
            int last = length-1;
            int mid,L;
                while(first<=last)
                {
                    mid = (first+last)/2;
                    if(track[mid]<sequence[i])
                    {
                        first = mid+1;
                    }
                    else
                    {
                        L = mid;
                        last = mid-1;
                    }
                }
             /* replacing */
            track[L] = sequence[i];
        }
    }
    return length;
}
int main() {
    
   /* 
    creating a vector to hold integer values. 
    Pushing our input sequence in the vector
    */
    vector<int> sequence={12,3,4,2,9,11,1,13,14,5,6,10};

   /*calling Long_Inc_SubSqnc function
     and passing out input sequence in it*/

    int max_length=Long_Inc_Subsqnc(sequence);
    cout<<max_length<<endl;
	return 0;
}
