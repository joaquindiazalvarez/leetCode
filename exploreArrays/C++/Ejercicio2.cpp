#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int even = 0;
        for(int i = 0; i < nums.size(); i++){
            int value = nums[i];
            int cont = 0;
            while(value > 0){
                value /= 10;
                cont++;

            }
            if(cont % 2 == 0){
                even++;
            }
        }
        return even;
    }
};
int main(){
    vector<int> v;
    v.push_back(12);
    v.push_back(245);
    v.push_back(2);
    v.push_back(6);
    v.push_back(7896);
    Solution sol;
    cout << sol.findNumbers(v);
}