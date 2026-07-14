class Solution {
public:
    int rob(vector<int>& nums) {
        int p1 = 0, p2 = 0, best = 0;
        for (int num : nums) {
            best = max(num+p2, p1);
            p2 = p1;
            p1 = best;
        }
        return p1;
    }
};
