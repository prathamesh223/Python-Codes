//Write an algorithm and program to count occurrence of a given character in a string
#include<iostream>
#include<bits\stdc++.h>
#include<string>
using namespace std;

int count_character(string str,char c)
{
    int count=0;
    for(int i=0;i<str.length();i++)
    {
        if(str[i]==c)
        {
            count++;
        }
    }
    return count;
}
int main()
{
    string str="hello";
    char c='l';
    cout<<"The character   "<<c<<"occurs  : "<<count_character(str,c)<<"  times"<<endl;

}
