class Solution {
public:
    int getSum(int a, int b) {
        int c = 0;
        int s = 0;
        int res = 0;

        for (int i=0; i<32; i++) {
            int bit_a = (a >> i) & 1;
            int bit_b = (b >> i) & 1;
            s = bit_a ^ bit_b ^ c;
            c = (bit_a & bit_b) | ((bit_a | bit_b) & c);
            res |= (s << i);
        }
        return res ;
    }
};
