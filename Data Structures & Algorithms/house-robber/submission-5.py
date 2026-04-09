class Solution:
    def rob(self, nums: List[int]) -> int:
        h1, h2 = 0,0
        for i in nums:
            max_amount = max(i+h2, h1)
            h2 = h1
            h1 = max_amount
        return h1