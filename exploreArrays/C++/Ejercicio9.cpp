#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        bool valid = true;
        int length = arr.size();
        int breakindex = length;
        if(arr.size() >= 3 && arr[0] < arr[1] && arr[length - 1] < arr[length - 2]){
            for(int i = 1; i < length; i++){
                if(arr[i] < arr[i-1]){
                    breakindex = i;
                    break;
                }
                if(arr[i] == arr[i-1]){
                    valid = false;
                    break;
                }
            }
            for(int i = length - 1; i > breakindex; i--){
                if(arr[i] > arr[i-1] || arr[i] == arr[i - 1]){
                    valid = false;
                }
            }
        }
        else{
            valid = false;
        }
        return valid;
    }
};
int main(){
    Solution MySolution;
    vector<int> vec = {14,82,89,84,79,70,70,68,67,66,63,60,58,54,44,43,32,28,26,25,22,15,13,12,10,8,7,5,4,3};
    cout << MySolution.validMountainArray(vec);
}
/* Example 1:

Input: arr = [2,1]
Output: false

Example 2:

Input: arr = [3,5,5]
Output: false

Example 3:

Input: arr = [0,3,2,1]
Output: true

[0,1,2,3,4,5,6,7,8,9]
false

[14,82,89,84,79,70,70,68,67,66,63,60,58,54,44,43,32,28,26,25,22,15,13,12,10,8,7,5,4,3]
false
 

Constraints:

    1 <= arr.length <= 104
    0 <= arr[i] <= 104
*/