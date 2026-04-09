class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i >= len(nums)-1:
                return True
            if nums[i] == 0:
                return False
            
            cache[i] = False
            for j in range(1,nums[i]+1):
                cache[i] |= dfs(i+j)
            
            return cache[i]
        
        return dfs(0)