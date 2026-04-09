class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        preList, prefix = [], 1
        postList, postfix = [], 1

        for i in range(len(nums)):
            products.append(prefix)
            prefix *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            products[i] *= postfix
            postfix *= nums[i]
        
        return products
