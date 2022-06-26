#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        bool exist = false;
        for(int i = 0; i < arr.size(); i++){
            for(int j = 0; j < arr.size(); j++){
                if(arr[j] == 2 * arr[i] && i != j){
                    exist = true;
                }
            }
        }
        return exist;
    }
};
int main(){
    Solution MySolution;
    vector<int> vec = {-2,0,10,-19,4,6,-8};
    cout << MySolution.checkIfExist(vec);


}

/*Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

Example 2:

Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.

Example 3:

Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.

[-2,0,10,-19,4,6,-8]
false
*/