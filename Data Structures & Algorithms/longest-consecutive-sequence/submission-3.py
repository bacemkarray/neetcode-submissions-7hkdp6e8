class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num-1 not in numSet:
                length = 1
                while num+1 in numSet:
                    num = num+1
                    length += 1
                longest = max(length, longest)
        return longest

                