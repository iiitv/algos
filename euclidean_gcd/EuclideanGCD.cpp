#include <bits/stdc++.h>
using namespace std;

int euclidean_gcd_recursive(int a, int b)
{
    if (a == 0)
        return b;
    return euclidean_gcd_recursive(b % a, a);
}

int euclidean_gcd_iterative(int a, int b) {
	while(b != 0) {  
		int temp = b;  
		b = a % b;
		a = temp;
	}
	return a;
}

int main() {
	int a = 69;
	int b = 11;
	int answer_recursive = euclidean_gcd_recursive(a, b);
	int answer_iterative = euclidean_gcd_iterative(a, b);
	cout<<"GCD of "<< a <<" and "<< b <<" is : "<< answer_recursive<<" by recursive algo"<<endl;
	cout<<"GCD of "<< a <<" and "<< b <<" is : "<<answer_iterative<<" by iterative algo"<<endl;
	return 0;
}
