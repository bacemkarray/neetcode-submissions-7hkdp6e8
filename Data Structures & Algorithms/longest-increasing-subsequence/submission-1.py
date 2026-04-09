class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i,j):
            if i == len(nums):
                return 0

            key = (i,j)
            if key in cache:
                return cache[key]

            res = dfs(i+1,j)

            if j == -1 or nums[i] > nums[j]:
                res = max(res, 1+dfs(i+1,i))
            
            cache[key] = res            
            return res
        
        return dfs(0,-1)