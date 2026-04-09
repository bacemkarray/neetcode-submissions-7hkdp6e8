class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        cache = {}

        def dfs(i,subset1, subset2):
            # key = (i,subset1, subset2)
            # if key in cache:
            #     return cache[key]

            if i == len(nums):
                return subset1 == subset2
            
            l = dfs(i+1,subset1+nums[i],subset2)
            r = dfs(i+1,subset1, subset2+nums[i])
            
            # cache[key] = l or r
            return l or r


        return dfs(0,0,0)