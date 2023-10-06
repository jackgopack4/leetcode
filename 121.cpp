#include <limits.h>
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size() == 1) {
            return 0;
        }
        int min_price = INT_MAX;
        int max_profit = 0;
        for(auto i=0;i<prices.size();++i) {
            if(prices[i] < min_price) {
                min_price = prices[i];
            }
            else if(prices[i] - min_price > max_profit) {
                max_profit = prices[i] - min_price;
            }
        }
        return max_profit;
    }
};
