class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if j == i:
        #             continue
        #         product *= nums[j]
        #     res.append(product)
        # return res

        res = []
        n = len(nums)
        preList, prefix = [1]*n, 1
        postList, postfix = [1]*n, 1
        for i in range(len(nums)):
            preList[i] = prefix
            prefix *= nums[i]
        
        for i in range(n-1, -1, -1):
            postList[i] = postfix
            postfix *= nums[i]
        
        for i in range(len(nums)):
            res.append(preList[i]*postList[i])
        
        return res

        