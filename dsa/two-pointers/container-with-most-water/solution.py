# Pattern: Two pointers
# Time: O(n) | Space: O(1)
# Tripped up on: Straight forward problem, just need to realize that we need to update the pointer with the smallest value.
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while l<r:
            area = min(heights[l], heights[r]) * (r-l)
            res = max(area, res)
            if heights[l] <= heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
        return res