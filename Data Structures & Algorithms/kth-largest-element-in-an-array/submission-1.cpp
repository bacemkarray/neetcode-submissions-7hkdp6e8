class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int> maxHeap(nums.begin(), nums.end());
        int i=0;
        int top;
        while (i<k) {
            top = maxHeap.top();
            maxHeap.pop();
            i++;
        }
        return top;
    }
};
