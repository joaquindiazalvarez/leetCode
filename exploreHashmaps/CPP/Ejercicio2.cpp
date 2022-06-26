#include <vector>
#include <iostream>
#include <string.h>
using namespace std;
class MyHashMap {
public:
    vector<int> keys;
    vector<int> values;

    void put(int key, int value) {
        if(alreadyExist(key) == true){
            values[searchKeyIndex(key)] = value;
        }
        else{
            keys.push_back(key);
            values.push_back(value);
        }
        
    }
    
    int get(int key) {
        if(searchKeyIndex(key) != -1){
            return(values[searchKeyIndex(key)]);   
        }
        else{
            return -1;
        }
    }
    
    void remove(int key) {
        if(alreadyExist(key)){
                int length = keys.size();
                int i = searchKeyIndex(key);
                    for(int j = i + 1; j < length; i++){
                        keys[j - 1] = keys[j];
                        values[j - 1] = values[j];
                    }
                keys.pop_back();
                values.pop_back();
            }
        }

    bool alreadyExist(int key) {
        bool exist = false;
        for(int i = 0; i < keys.size(); i++){
            if(keys[i] == key){
                exist = true;
            }
        }
        return exist;
    }
    int searchKeyIndex(int key){
        for(int i = 0; i < keys.size(); i++){
            if(keys[i] == key){
                return i;
            }
        }
        return -1;
    }
};
int main(){
    MyHashMap myHashMap;
    myHashMap.put(1, 1);
    myHashMap.put(2, 2);
    cout << myHashMap.get(1);
    cout << myHashMap.get(3);
    myHashMap.put(2, 1);
    cout << myHashMap.get(2);
    myHashMap.remove(2);
    cout << myHashMap.get(2);
}
/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */
/*
Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
*/