// 747. Largest Number At Least Twice of Others
/* 
You are given an integer array nums where the largest integer is unique.
Determine whether the largest element in the array is at least twice as much as 
every other number in the array. If it is, return the index of the largest element, 
or return -1 otherwise.
*/
#import <iostream>
#include <string>
using namespace std;
class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int largest_index {-1};
        int second_largest_index {-1};
        int largest {0};
        int second_largest {0};
        for(auto i=0; i<nums.size(); ++i) {
            //cout << "i="+std::to_string(i)+"\n";
            if(nums[i]>largest) {
                second_largest = largest;
                second_largest_index = largest_index;
                largest = nums[i];
                largest_index = i;
            }
            else if((largest > nums[i]) && (nums[i] > second_largest)) {
                second_largest = nums[i];
                second_largest_index = i;
            }
        }
        //cout << "largest="+std::to_string(largest)+", index="+std::to_string(largest_index)+"\n";
        //cout << "second largest="+std::to_string(second_largest)
                                                 +", index="+std::to_string(second_largest_index)+"\n";
        if(second_largest == 0) {
            return largest_index;
        }
        else if((largest / second_largest) >= 2) {
            return largest_index;
        }
        else {
            return -1;
        }
    }
};
