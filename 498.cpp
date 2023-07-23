// 498. Diagonal Traverse
/*
  Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
*/

class Solution {
public:
    static constexpr int upRight = 0;
    static constexpr int downLeft = 1;
    static constexpr int down = 2;
    static constexpr int right = 3;
    int vert_max_index;
    int hor_max_index;
    void moveUpRight(vector<int>& coord) {
        --coord[0];
        ++coord[1];
    }
    void moveDownLeft(vector<int>& coord) {
        ++coord[0];
        --coord[1];
    }
    void moveDown(vector<int>& coord) {
        ++coord[0];
    }
    void moveRight(vector<int>& coord) {
        ++coord[1];
    }
    int chooseDirection(vector<int>& coord, int& last) {
        switch(last) {
            case upRight: {
                if(coord[0] > 0) {
                    if(coord[1] < hor_max_index) {
                        return upRight;
                    }
                    else {
                        return down;
                    }
                }
                else {
                    if(coord[1] < hor_max_index) {
                        return right;
                    }
                    else {
                        return down;
                    }
                }
                break;
            }
            case right: {
                if(coord[0] == vert_max_index) {
                    return upRight;
                }
                else {
                    return downLeft;
                }
                break;
            }
            case downLeft: {
                if(coord[0] < vert_max_index) {
                    if(coord[1] > 0) {
                        return downLeft;
                    }
                    else {
                        return down;
                    }
                }
                else {
                    return right;
                }
                break;
            }
            default: {
                // last = down
                if(coord[1] < hor_max_index) {
                    return upRight;
                }
                else {
                    return downLeft;
                }
            }
        }
    }
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        int hor_length {static_cast<int>(mat[0].size())};
        int vert_length {static_cast<int>(mat.size())};
        vert_max_index = vert_length - 1;
        hor_max_index = hor_length - 1;
        // take care of special case 1x1 or 1xn
        vector<int> result {};
        if(vert_length == 1) {
            return mat[0];
        }
        else if(hor_length == 1) {
            for(auto n: mat) {
                result.push_back(n[0]);
            }
            return result;
        }
        else {
            int size {hor_length * vert_length};
            
            int dir = upRight;
            // first index of coord is vertical array, second is horizontal position in array
            vector<int> coord{0,0};
            for(auto k=0;k<size;++k) {
                result.push_back(mat[coord[0]][coord[1]]);
                dir = chooseDirection(coord,dir);
                switch(dir) {
                    case upRight: {
                        moveUpRight(coord);
                        break;
                    }
                    case right: {
                        moveRight(coord);
                        break;
                    }
                    case downLeft: {
                        moveDownLeft(coord);
                        break;
                    }
                    default: {
                        moveDown(coord);
                    }
                }
            }
            return result;
        }
        
    }
};
