class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev = nums[0]
        curr = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            best = max(nums[i] + prev, curr)
            prev = curr
            curr = best




            

        return curr

        