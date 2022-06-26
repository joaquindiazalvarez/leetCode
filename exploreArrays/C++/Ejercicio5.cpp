#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
      for(int i = m; i < nums1.size(); i++){
          nums1[i] = nums2[i-m];
      }
      sort(nums1.begin(), nums1.end());

    }
};
int main(){
    vector<int> vec1 = {1,2,3,0,0,0};
    vector<int> vec2 = {3,2,1};
    int m = 3;
    int n = 3;
    Solution sol;
    sol.merge(vec1, m, vec2, n);
    for(int i = 0; i < vec1.size(); i++){
        cout << vec1[i] << ","; 
    }


}