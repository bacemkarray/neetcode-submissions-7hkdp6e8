class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_length = 0
        i = 0
        while i < len(nums):
            length = 1
            num = nums[i]
            while num+1 in nums:
                num += 1
                length += 1
            i += 1

            longest_length = max(longest_length, length)

        return longest_length
