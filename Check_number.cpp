//Program to check if a number is Positive, Negative, Odd, Even, Zero
#include<iostream>
using namespace std;
int main()
{
    int num;
    cout<<"Enter a number:";
    cin>>num;
    if(num>0)
    {
        cout<<"The number is Positive";
    }
    else if(num<0)
    {
        cout<<"The number is Negative";
    }
    else
    {
        cout<<"The number is Zero";
    }
    if(num%2==0)
    {
        cout<<" and Even";
    }
    else
    {
        cout<<" and Odd";
    }
}