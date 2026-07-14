class Solution:
    def rob(self, nums: List[int]) -> int:
        p1, p2, best = 0,0,0

        for num in nums:
            best = max(p2+num,p1)
            p2 = p1
            p1 = best
        
        return p1