#include<iostream>
#include<vector>
using namespace std;

int main()
{
    vector<int>v;//Initia;ize empty vector
    vector<int>a(6,1);
    for (int i:a)
    {
        cout<<i<<" ";
    }
    cout<<endl;
    vector<int>l(a);//Copy vector a in l
    for (int i:l)
    {
        cout<<i<<" ";
    }

    cout << "capacity->" << v.capacity() << endl;

    v.push_back(1);
    cout << "capacity->" << v.capacity() << endl;//Push back is used add element in the vector

    v.push_back(2);
    cout << "capacity->" << v.capacity() << endl;

    v.push_back(3);
    cout << "capacity->" << v.capacity() << endl;//Dynamically capacity of container gets double when 3 is pushback
    cout << "Size " << v.size() << endl;
    cout << "Front " << v.front()<<endl;
    cout << "Back " << v.back();

    cout << endl << "Before pop" << endl;
    for (int i : v) {
        cout << i << endl;
    }

    cout << endl << "After pop" << endl;

    v.pop_back();
    for (int i : v) {
        cout << i << endl;
    }
    return 0;


}
