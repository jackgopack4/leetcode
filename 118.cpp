// 118. Pascal's Triangle
/*
  Given an integer numRows, return the first numRows of Pascal's triangle.
  In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
*/
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> result {};
        for(auto i=0;i<numRows;++i) {
            if(i==0) {
                result.push_back(vector<int>{1});
            }
            else if(i==1) {
                result.push_back(vector<int>{1,1});
            }
            else {
                vector<int> row {};
                for(auto j=0;j<=i;++j) {
                    if(j==0 || j==i) {
                        row.push_back(1);
                    }
                    else {
                        row.push_back(result[i-1][j-1]+result[i-1][j]);
                    }
                }
                result.push_back(row);
            }
        }
        return result;
    }
};
