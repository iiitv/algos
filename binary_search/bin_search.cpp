#include<bits/stdc++.h>
#include<algorithm>
using namespace std;

int a[10]={7,10,22,30,33,45,66,72,83,100};
int binsearch(int st,int en,int el)
  {
    int mid=(st+en)/2;

     if(el>a[en]||el<a[st])
        {return 0;}

    if(el==a[mid])
    {return mid;}

    else if(el<a[mid])
      {binsearch(st,mid,el);}

    else if(el>a[mid])
      {binsearch(mid,en,el);}
    }

int main()
  {int i=10;  //can change depending on the size of the array
    int el;
    //sort(a,a+i-1);

      cout<<"enter the elemnt to be searched: ";
      cin>>el;

    if(binsearch(0,i-1,el)==0)
        {cout<<"the elemnt does not exist";}

    else
          {cout<<"the element you have been searching for is at index: "<<binsearch(0,i-1,el);}


    return 0;}
