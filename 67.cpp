// 67. Add Binary
// Given two binary strings a and b, return their sum as a binary string.
#include <string>
class Solution {
public:
    char addDigit(const char& a, const char& b, char& overflow) {
        if(overflow == '1') {
            if(a == '0') {
                if(b == '0') {
                    overflow = '0';
                    return '1';
                }
                else {
                    return '0';
                }
            }
            else { //a == '1'
                if(b == '0') {
                    return '0';
                }
                else {
                    return '1';
                }
            }
        }
        else {
            if(a == '0') {
                return b;
            }
            else {
                if(b == '0') {
                    return a;
                }
                else {
                    overflow = '1';
                    return '0';
                }
            }
        }
        return '0';
    }
    string addBinary(string a, string b) {
        std::string a_string = std::string(a);
        std::string b_string = std::string(b);
        int a_length {static_cast<int>(a_string.size())};
        int b_length {static_cast<int>(b_string.size())};
        char overflow{'0'};
        std::string result = std::string();
        if(a_length > b_length) {
            b_string.insert(0,a_length-b_length,'0');
            b_length = a_length;
        }
        else if(b_length > a_length) {
            a_string.insert(0,b_length-a_length,'0');
            a_length = b_length;
        }
        std::cout << "a_string: "+a_string+"\n";
        std::cout << "b_string: "+b_string+"\n";
        for(auto i=a_length-1;i>=0;--i) {
            result.insert(result.begin(),addDigit(a_string[i],b_string[i],overflow));
        }
        if(overflow == '1') {
            result.insert(result.begin(),overflow);
        }
        return result;
    }
};
