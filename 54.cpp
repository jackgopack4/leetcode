// 54. Spiral Matrix
/*
  Given an m x n matrix, return all elements of the matrix in spiral order.
*/

#import <iostream>
#include <string>
#include <algorithm>

class Solution {
public:
    static constexpr int down = 0;
    static constexpr int up = 1;
    void printResult(vector<int>& result) {
        std::cout << "result after push: [";
                        for(auto r : result) {
                            std::cout<< std::to_string(r) << " ";
                        }
                        std::cout <<"]\n";
    }
    void printCoord(vector<int>& coord) {
        std::cout << "coord = ["+std::to_string(coord[0])+", "+std::to_string(coord[1])+"]\n";
    }
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m_min {0};
        int m_max {static_cast<int>(matrix.size())-1};
        int n_min {0};
        int n_max {static_cast<int>(matrix[0].size())-1};
        int size = (m_max+1) * (n_max+1);
        vector<int> coord {0,0};
        vector<int> result {};
        int dir = up;
        auto i = 0;
        //std::cout << "size = "+std::to_string(size)+"\n";
        while(i<size) {
            switch(dir) {
                case up: {
                    if(coord[0] == m_min) {
                        result.insert(result.end(), matrix[m_min].begin()+n_min, 
                                      matrix[m_min].end()-(matrix[m_min].size()-n_max-1));
                        //printResult(result);
                        i+= (n_max-n_min+1);
                        if(coord[0] > 0) {
                            ++n_min;
                        }
                        coord[0] = ++m_min;
                        coord[1] = n_max;
                        //printCoord(coord);
                        dir = down;
                    }
                    else {
                        result.push_back(matrix[coord[0]][coord[1]]);
                        //printResult(result);
                        --coord[0];
                        //printCoord(coord);
                        ++i;
                    }
                    break;
                }
                default: {
                    if(coord[0] == m_max) {
                        std::reverse(matrix[m_max].begin()+n_min,matrix[m_max].end()-
                                     (matrix[m_max].size()-n_max-1));
                        result.insert(result.end(), matrix[m_max].begin()+n_min, 
                                      matrix[m_max].end()-(matrix[m_max].size()-n_max-1));
                        //printResult(result);
                        i+=(n_max-n_min+1);
                        coord[0] = --m_max;
                        coord[1] = n_min;
                        //printCoord(coord);
                        --n_max;
                        //std::cout << "n_max = "+std::to_string(n_max)+"\n";
                        dir = up;
                    }
                    else {
                        result.push_back(matrix[coord[0]][coord[1]]);
                        //printResult(result);
                        ++coord[0];
                        //printCoord(coord);
                        ++i;
                    }
                }
            }
            //std::cout << "i = "+std::to_string(i)+"\n";
        }
        return result;
    }
};
