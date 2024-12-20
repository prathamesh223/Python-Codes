// // . Intersection of Two Arrays II
// Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

// Example 1:

// Input: nums1 = [1,2,2,1], nums2 = [2,2]
// Output: [2,2]
// Example 2:

// Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
// Output: [4,9]
// Explanation: [9,4] is also accepted.
//Unordered Map or Hash table with time  complexity O(1)
#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;
vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int,int>mp;
        vector<int>res;
        for(int i:nums1)
        {
            mp[i]++;
        }
        for(int i:nums2)
        {
            if(mp[i]>0)
            {
                res.push_back(i);
                mp[i]--;
            }
        }
        return res;
    }

int main()
{
    vector<int>nums1={1,2,2,1};
    vector<int>nums2={2,2};
    vector<int>res=intersect(nums1,nums2);
    for (int i:res)
    {
        cout<<i<<" ";
    }
    return 0;
}