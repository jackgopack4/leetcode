// 66. Plus One
/*
You are given a large integer represented as an integer array digits, where each digits[i] 
is the ith digit of the integer. The digits are ordered from most significant to least 
significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
*/

#include <iostream>
#include <iterator>
#include <vector>

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        bool carryover = true;
        vector<int> result {digits};
        int i {static_cast<int>(result.size()-1)};
        while(carryover && (i >= 0)) {
            if(result[i] == 9) {
                    result[i] = 0;
                    if(i == 0) {
                        auto it = result.begin();
                        it = result.insert(it,1);
                    }
            }
            else {
                result[i]+=1;
                carryover = false;
            }
            --i;
        }
        return result;
    }
};
