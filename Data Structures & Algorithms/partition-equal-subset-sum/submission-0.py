class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(i,subset1, subset2):
            if i == len(nums):
                return subset1 == subset2
            
            l = dfs(i+1,subset1 + nums[i],subset2)
            r = dfs(i+1,subset1,subset2 + nums[i])
            if l or r:
                return True
            return False


        return dfs(0,0,0)