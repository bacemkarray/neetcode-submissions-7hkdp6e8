class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # products = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         product *= nums[j]
        #     products.append(product)
        # return products

        products = []
        preList, prefix = [], 1
        postList, postfix = [], 1

        for i in range(len(nums)):
            preList.append(prefix)
            prefix *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            postList.append(postfix)
            postfix *= nums[i]
        
        postList.reverse()
        for i in range(len(nums)):
            products.append(preList[i]*postList[i])
        
        return products
