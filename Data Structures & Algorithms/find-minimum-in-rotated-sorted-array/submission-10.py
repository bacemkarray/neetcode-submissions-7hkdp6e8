class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        minimum = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                # return nums[left] # know its sorted
                minimum = min(minimum, nums[left])
            
            middle = (left + right)//2
            # if nums[left] <= nums[middle]:
            if nums[left] <= nums[middle]:
                left = middle + 1

            else:
                right = middle - 1
            
            minimum = min(minimum, nums[middle])
        
        return minimum