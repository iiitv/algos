//Time: O(n*log(n))
#include <bits/stdc++.h>
using namespace std;

int LIS(vector<int> A) {
	if(A.size()<=1) return A.size();
	vector<int> S;
	S.push_back(A[0]);
	for(int i=1; i<A.size(); i++){
		if(A[i]>S[S.size()-1]) S.push_back(A[i]);
		else{
			int start=0;
			int end=S.size()-1;
			while(start<=end){
				int mid=start+(end-start)/2;
				if(S[mid]>=A[i])  end=mid-1;
				else start=mid+1;
			}
			S[end+1]=A[i];
		}
	}
	return S.size();
}
int main(){
	int n; cin >> n; // size of array for which LIS needs to be found
	vector<int> V(n);
	for(int i=0; i<n; i++) cin >> V[i]; //input of vector
	cout << LIS(V) << endl;
}
