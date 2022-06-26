#include <vector>
#include <string>
#include <iostream>

using namespace std;
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max = -1;
        int cont = 0;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] == 1){
                cont++;
            }
            else if(nums[i] == 0){
                if(cont > max){
                    max = cont;
                }
                cont = 0;
            }
        if(cont > max){
            max = cont;
            }
        }
        return max;
    }
};
int main(){
    vector<int> vect;
    vect.push_back(1);
    vect.push_back(1);
    vect.push_back(0);
    vect.push_back(1);
    vect.push_back(1);
    vect.push_back(1);
    for (int i = 0; i < vect.size(); i++)
        cout << vect[i] <<",";
    cout << "\n";
    Solution sol1;
    cout << sol1.findMaxConsecutiveOnes(vect);
}