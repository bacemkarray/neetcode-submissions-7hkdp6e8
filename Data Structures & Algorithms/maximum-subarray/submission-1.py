class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subArray = nums[0]
        glob = nums[0]
        for i in range(1,len(nums)):
            subArray = max(nums[i], subArray + nums[i])
            if subArray > glob:
                glob = subArray

        return glob
            
 
        # return subArray
        # best = nums[0]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)+1):
        #         best = max(sum(nums[i:j]), best) 

        # return best

             