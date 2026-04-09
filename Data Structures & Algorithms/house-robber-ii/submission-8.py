class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def search(houses):
            ptr1,ptr2 = 0, 0
            for i in houses:
                max_prof = max(i + ptr2, ptr1)
                ptr2 = ptr1
                ptr1 = max_prof
            return max_prof
        

        return max(search(nums[:-1]), search(nums[1:]))