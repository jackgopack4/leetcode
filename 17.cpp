#include <map>
#include <iostream>
#include <string>
using namespace std;
class Solution {
public:
    std::map<int, vector<string>> m;
    vector<string> letterCombinations(string digits) {
        vector<string> v2 = {"a","b","c"};
        m[2] = v2;
        vector<string> v3 = {"d","e","f"};
        m[3] = v3;
        vector<string> v4 = {"g","h","i"};
        m[4] = v4;
        vector<string> v5 = {"j","k","l"};
        m[5] = v5;
        vector<string> v6 = {"m","n","o"};
        m[6] = v6;
        vector<string> v7 = {"p","q","r","s"};
        m[7] = v7;
        vector<string> v8 = {"t","u","v"};
        m[8] = v8;
        vector<string> v9 = {"w","x","y","z"};
        m[9] = v9;
        vector<string> res{};
        for(auto i=0;i<digits.length();++i) {
            auto cur_val = std::stoi(digits.substr(i,1));
            auto cur_letters = m[cur_val];
            auto prev_res_length = res.size();
            for (auto j=1;j<cur_letters.size();++j) {
                for (auto k=0;k<prev_res_length;++k) {
                    res.push_back(res[k]);
                }
            }
            /*
            cout << "res: [";
            for(int j=0;j<res.size();++j) {
                cout << res[j] << " ";
            }
            cout << "] \n";
            */
            if(i == 0) {
                res.insert(res.end(),cur_letters.begin(),cur_letters.end());
                //res.extend(cur_letters);
                /*
                cout << "res after extend: [";
                for(int j=0;j<res.size();++j) {
                    cout << res[j] << " ";
                }
                cout << "] \n";
                */
            }
            else {
                for (auto j=0;j<cur_letters.size();++j) {
                    for (auto k=0;k<prev_res_length;++k) {
                        res[k+j*prev_res_length].append(cur_letters[j]);
                    }
                }
                /*
                cout << "res after extend: [";
                for(int j=0;j<res.size();++j) {
                    cout << res[j] << " ";
                }
                cout << "] \n";
                */
            }

        }
        return res;
    }
};
