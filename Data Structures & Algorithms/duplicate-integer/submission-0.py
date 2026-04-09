class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if num in num_dict - > return true else add num to num_dict
        num_dict = {}
        for num in nums:
            if num in num_dict:
                return True
            num_dict[num] = 0
        return False