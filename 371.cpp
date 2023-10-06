using namespace std;
class Solution {
public:
    int getSum(int a, int b) {
        //cout << "num bits: " << bits << "\n";
        int res = 0;
        uint32_t and_shift = 1;
        bool carry_bit = false;
        for(auto i=0;i<sizeof(a)*8;++i) {
            uint32_t a_tmp = a & and_shift;
            uint32_t b_tmp = b & and_shift;
            if(!(!a_tmp != !b_tmp) != !carry_bit) { //logical xor
                res |= and_shift;
            }
            if(a_tmp & b_tmp || a_tmp && carry_bit || b_tmp && carry_bit) {
                carry_bit = true;
            }
            else {
                carry_bit = false;
            }
            and_shift <<=1;
        }
        return res;
    }
};
