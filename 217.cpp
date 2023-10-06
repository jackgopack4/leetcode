#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::unordered_set<int> seen{};
        for(int n: nums) {
            if (seen.contains(n)) {
                return true;
            }
            else {
                seen.insert(n);
            }
        }
        return false;
    }
};
