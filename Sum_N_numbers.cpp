#include<iostream>
using namespace std;

int findsum(int n)
{
    return n * (n+1)/2;
}
int main()
{
    int n;
    cout<<"Enter a number:";
    cin>>n;
    cout<<"The sum of first "<<n<<" natural numbers is "<<findsum(n);
    return 0;
}