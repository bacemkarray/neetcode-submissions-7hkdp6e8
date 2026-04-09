class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd, minProd = 1,1
        res = max(nums)

        for n in nums:
            temp = maxProd*n
            maxProd = max(maxProd*n, minProd*n, n)
            minProd = min(temp, minProd*n, n)
            res = max(res, maxProd)
        return res

        
