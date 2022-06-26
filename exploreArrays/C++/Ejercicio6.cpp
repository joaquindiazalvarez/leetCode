#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int length = 0;
        for(int i = 0; i< nums.size(); i++){
            length++;
        }
        for(int i = 0; i < length; i++){
            while(nums[i] == val && i < length){
                for(int j = i + 1; j < length; j++){
                    nums[j - 1] = nums[j];
                }
                length--;
            }
        }
        return length;
    }
};
int main(){
    vector<int> vec = {0, 1, 2, 2, 3, 0, 4, 2};
    Solution sol;
    cout << sol.removeElement(vec, 2);
    for(int i = 0; i< vec.size(); i++){
        cout << vec[i];
    }    
}


