// You are going to travel to another city that is located 𝑑 miles away from your home city. Your car can travel
// at most 𝑚 miles on a full tank and you start with a full tank. Along your way, there are gas stations at
// distances stop1, stop2, . . . , stop𝑛 from your home city. What is the minimum number of refills needed?
//Time Complexity of the implementation : O(n^2)
#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    //d is the distance between the starting point and the destination.
    //m is the maximum distance the car can travel with a full tank.
    //n is the number of refill stops between the starting point and destination.
    ll d, m, n;
    cin >> d >> m >> n;
    //Array a stores the distance (from the starting point) at which the refill stops are located.
    ll a[n + 2];
    a[n + 1] = d; //n+1th position is initiallized to the destination, since it will be a stop.
    a[0] = 0;     //0th position is the position from where we start.
    for (ll i = 1; i <= n; i++)
    {
        cin >> a[i];
    }
    ll currRefill = 0; //currRefill stores the index of the array a i.e. where car is standing
    ll numRefill = 0;  //numRefill counts the number of refills we make on our way to destination
                       //it is initialized to 0, since we are at the start
    ll flag = 0;       //flag is used to check if it's impossible to complete the journey
    while (currRefill <= n)
    {
        ll lastRefill = currRefill;
        while ((currRefill <= n)                              //checking if we haven't reached the destination i.e. index of array a <= n
               && ((a[currRefill + 1] - a[lastRefill]) <= m)) //checking if he have enough fuel to travel to the further refill stop
            currRefill++;                                     //increasing the index of the array a i.e. we are moving to the next refill stop

        if (currRefill == lastRefill) //checking if the previous refill stop is equal to the current refill stop
                                      //if that's the case, then we don't have enough fuel to move to the next stop
                                      //and hence it is impossible to complete the journey
        {
            flag = 1; //so we turn the flag to the value 1
            break;    //and break out since no use of iterating further in the array a i.e. we know we can't move further in our journey
        }
        else if (currRefill <= n) //if we land here, it means we don't have enough fuel to make up to the next refill stop
                                  //so we refill at the current refill stop
            numRefill++;          //increasing the numRefill since we make refill at the current refill stop
    }
    if (flag == 0)
        cout << numRefill << endl; //printing minimum number of refills made.
    else
        cout << "-1" << endl; //printing -1 if it's impossible to complete the journey.

    return 0;
}
