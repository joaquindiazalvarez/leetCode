#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        for(int i = 0; i < arr.size(); i++){
            if(arr[i] == 0){
                for(int j = arr.size() - 2; j >= i; j--){
                    arr[j + 1] = arr[j];
                }
                arr[i] = 0;
                i++;
            }
        }
    }
};
int main(){
    vector<int> vec = {1,0,2,3,0,4,5,0};
    Solution sol;
    sol.duplicateZeros(vec);
    for(int i = 0; i < vec.size(); i++){
        cout << vec[i] << ",";
    }
}