class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Use a hashmap. Check if target - current element is equal to something in the hashmap. If not,
        #append elements to a hashmap.
        num_dict = {}
        
        for i, num in enumerate(nums):
            if target-num in num_dict:
                return [num_dict[target-num], i]
            num_dict[num] = i
        