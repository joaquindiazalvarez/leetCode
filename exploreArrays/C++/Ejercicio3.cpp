#include <vector>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums){
        vector<int> arr;
        int power;
        int base;
        for(int i = 0; i < nums.size(); i++){
            base = nums[i];
            power = pow(base, 2);
            arr.push_back(power);
        }
        sort(arr.begin(), arr.end());
        return arr;
    }
};
int main(){
    vector<int> vec = {4,3,5};
    vec.push_back(3);
    vec.push_back(2);
    vec.push_back(1);
    Solution sol;
    vector<int> solu = sol.sortedSquares(vec);
    for(int i = 0; i < solu.size(); i++){
        cout << solu[i] << ","; 
    }
}