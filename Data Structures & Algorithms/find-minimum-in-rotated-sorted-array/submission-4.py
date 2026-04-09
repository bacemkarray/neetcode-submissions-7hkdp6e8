class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest = nums[0]
        low = 0
        high = len(nums)-1

        while low <= high:
            if nums[low] < nums[high]:
                smallest = min(smallest, nums[low])
                break
            
            mid = (low+high)//2
            smallest = min(smallest, nums[mid])
            if nums[mid] >= nums[low]:
                low = mid+1
            else:
                high = mid-1
        
        return smallest



            
        