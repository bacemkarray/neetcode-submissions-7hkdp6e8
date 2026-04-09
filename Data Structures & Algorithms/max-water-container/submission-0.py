class Solution:
    def maxArea(self, heights: List[int]) -> int:
        greatest_area = 0
        l = 0
        r = len(heights)-1
        while l < r:
            if heights[l] < heights[r]:
                area = (r-l)*heights[l]
                l += 1
            else:
                area = (r-l)*heights[r]
                r -= 1
            
            if area > greatest_area:
                greatest_area = area
            
        return greatest_area