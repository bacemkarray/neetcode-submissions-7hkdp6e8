class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> res;
        int l=0;
        int r=numbers.size()-1;
        while (l<r) {
            int sum = numbers[l] + numbers[r];
            if (sum == target) {
                res = {l+1, r+1};
                break;
            }
            else if (sum > target) r--;
            else l++;

        }
        return res;
    }
};
