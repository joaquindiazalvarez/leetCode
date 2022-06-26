#include <vector>
#include <iostream>
using namespace std;

class MyHashSet {
public:
    vector<int> set;    
    void add(int key) {
        if(contains(key) == false){
            set.push_back(key);    
        }
    }
    
    void remove(int key) {
        if(contains(key)==true){
            int length = set.size();
            for(int i = 0; i < length; i++){
                if(set[i] == key){
                    for(int j = i + 1; j < length; j++){
                        set[j - 1] = set[j];
                    }
                }
            }
            set.pop_back();
        }
    }
    
    bool contains(int key) {
        bool exist = false;
        for(int i = 0; i < set.size(); i++){
            if(set[i] == key){
                exist = true;
            }
        }
        return exist;
    }
};
int main(){
    MyHashSet set1;
    set1.add(1);
    set1.add(2);
    set1.contains(1);
    set1.contains(3);
    set1.add(2);
    set1.contains(2);
    set1.remove(2);
    set1.contains(2);
    cout << "contiene 2? "<<set1.contains(2);
    for(int i = 0; i < set1.set.size(); i++){
        cout << set1.set[i];
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
//["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]
//[[],[1],[2],[1],[3],[2],[2],[2],[2]]