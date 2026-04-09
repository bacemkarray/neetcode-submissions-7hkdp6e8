class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> lookup;
        vector<int> res;
        for (int i=0; i<nums.size(); i++) {
            int diff=target-nums[i];
            if (lookup.find(diff) != lookup.end()) {
                res = {lookup[diff], i};
                return res;
            }
            lookup[nums[i]] = i;
        }
        return res;
    }
};
