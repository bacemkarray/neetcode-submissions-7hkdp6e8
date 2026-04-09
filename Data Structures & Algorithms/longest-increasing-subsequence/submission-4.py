class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(i,j):
            if i == len(nums):
                return 0

            LIS = dfs(i+1,j)
            
            if j == -1 or nums[i] > nums[j]:
                LIS = max(dfs(i+1,i)+1,LIS)

            return LIS
            
            
        return dfs(0,-1)