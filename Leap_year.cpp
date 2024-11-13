#include<iostream>
using namespace std;
bool Checkyear(int year)
{
    if(year%4==0)
    {
        if(year%100 ==0)
        {
            return year%400==0;
        }
        return true;
    }
    return false;
}
int main()
{
    int year;
    cout<<"Enter the year:";
    cin>>year;
    if (Checkyear(year))
    {
        cout<<year<<" is a leap year"<<endl;
    }
    else
    {
        cout<<year<<" is not a leap year"<<endl;
    }
    return 0;
}