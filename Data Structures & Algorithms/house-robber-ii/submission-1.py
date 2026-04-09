class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        
        def search(nums):
            rob1, rob2 = 0,0
            for i in nums:
                res = max(i+rob2, rob1)
                rob2 = rob1
                rob1 = res
            return rob1

        return max(search(nums[1:]), search(nums[:-1]))






                    









