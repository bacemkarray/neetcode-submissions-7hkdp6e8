class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for num in numsSet:
            if num-1 not in numsSet:
                length = 1
                while num+1 in numsSet: # O(1) lookup cuz of set as opposed to array
                    length += 1
                    num = num+1
                longest = max(longest, length)
        return longest

                    
