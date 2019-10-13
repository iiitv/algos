#include <iostream>
using namespace std;
int exponentiationBySquaring(int base, int power) {
    if(power < 0) 
        return exponentiationBySquaring(1/base, -power);
    else if(power == 0) {
        return 1; //Because anythign raised to the power 0 is 1.
    }
    else if(power == 1)
        return base; // Return Base number if power is 1.
    else if(power %2 == 0)
        return exponentiationBySquaring(base * base , power/2 ) ;
    else  
        return base * exponentiationBySquaring(base* base, (power-1)/2); 
}
int main()
{
    cout<<exponentiationBySquaring(12,2);
    return 0;
}
