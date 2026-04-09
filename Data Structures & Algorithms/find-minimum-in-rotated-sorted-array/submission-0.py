class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest = 1001

        for num in nums:
            smallest = min(smallest, num)
        
        return smallest