class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def max_profit(houses):
            rob1, rob2 = 0,0
            for h in houses:
                best = max(h+rob2, rob1)
                rob2 = rob1
                rob1 = best
            return rob1
            
        return max(max_profit(nums[1:]), max_profit(nums[:-1]))