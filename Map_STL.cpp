#include<iostream>
#include<map>
using namespace std;
int main()
{
    map<int,string>m;
    //sorted in the case of map
    //unsorted in the case of unordered map implemented using the hash table
    // for search unsorted map have time complexity of O(1)
    //Sorted map is implemented using the red black tree.
    //sorted map have time complexity of O(logn)
    m[1]="Prathamesh";
    m[2]="Shivraj";
    m[3]="Akash";
    m[4]="Pradnya";
    for (auto i:m)
    {
        cout<<i.first<<" "<<i.second<<endl;
    }
    cout<<"Size of map is "<<m.size()<<endl;
    cout<<"Max size of map is "<<m.max_size()<<endl;
    m.insert({5,"Sharda"});
    for (auto i:m)
    {
        cout<<i.first<<" "<<i.second<<endl;
    }
    cout<<"Check 3 is present or not-> "<<m.count(3)<<endl;
     m.erase(1);
  cout<<"After erase"<<endl;
  for (auto i:m){
  
    cout<<i.first<<" "<<i.second<<endl;

  } 
}