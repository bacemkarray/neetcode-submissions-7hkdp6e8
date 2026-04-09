class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_prof_0 = 0
        max_prof_1 = 0

        ptr1,ptr2 = 0, 0
        for i in nums[1:]:
            max_prof_0 = max(i + ptr2, ptr1)
            ptr2 = ptr1
            ptr1 = max_prof_0
        
        ptr1,ptr2 = 0, 0
        for i in nums[:-1]:
            max_prof_1 = max(i + ptr2, ptr1)
            ptr2 = ptr1
            ptr1 = max_prof_1

        return max(max_prof_0, max_prof_1)