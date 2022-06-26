#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int length = nums.size();
        int cont = 0;
        for(int i = 1; i < length; i++){
            if(nums[i -1] != nums[i]){
                for(int j = i; j < length; j++){
                        nums[j-cont] = nums[j];
                }
                i=i-cont;
                length-=cont;
                cont = -1;
            }
            cont++;
            if(i==length-1){
                length-=cont;
            }
        }
        return length;       
    }
};
int main(){
    vector<int> vec = {1,1,2};
    Solution sol;
    cout << sol.removeDuplicates(vec);
    for(int i = 0; i < vec.size(); i++){
        cout << vec[i] << ",";
    }
}
//nums = [0,0,1,1,1,2,2,3,3,4]
//Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
//Input nums = [1,1]
//Output = 1, [1]
//Input [1,1,2]
//Output[1,2]