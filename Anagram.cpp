#include <iostream>
#include <algorithm>
using namespace std;

bool isAnagram(string str1, string str2) {
    if (str1.length() != str2.length())
        return false;
    sort(str1.begin(), str1.end());
    sort(str2.begin(), str2.end());
    return (str1 == str2);
}

int main() {
    string s1 = "listen";
    string s2 = "silent";
    if (isAnagram(s1, s2))
        cout << "Anagram" << endl;
    else
        cout << "Not anagram" << endl;
    return 0;
}
