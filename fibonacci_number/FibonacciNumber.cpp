#include <iostream>

using namespace std;

//function to return nth fibonacci number
int fibonacci(int n)
{
    if(n == 1 || n == 2){
        return n-1;
    }
    
    int a = 0;//second last fibonacci number
    int b = 1;//last fibonacci number
    int sum = 0;//current fibonacci number
    
    for (int i = 2; i < n; i++) {
        sum = a + b;
        a = b;
        b = sum;
    }
    return sum;
}

int main()
{
    int n = 7;
    if(n <= 0){
        cout << "n must be always be greater than 0.";
        return 0;
    }
    cout << fibonacci(n);
    return 0;
}
