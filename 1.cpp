#include <unordered_map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
        vector<int> result{};
        std::unordered_map<int, int> seen{};
        for(auto i = 0; i < nums.size(); ++i)
        {   
            int tmp = target - nums[i];
            if(seen.contains(tmp))
            {
                result.push_back(seen[tmp]);
                result.push_back(i);
                return result;
            }
            if(!seen.contains(nums[i]))
            {
                seen[nums[i]] = i;
            }
        }
        return result;
    }
};
