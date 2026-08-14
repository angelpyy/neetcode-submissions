class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = 0

        l = 0
        r = len(heights) - 1
        while l < r:
            width = r - l
            height = min(heights[r],heights[l])

            v = width * height

            volume = max(volume, v)

            if heights[l] >= heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
        
        return volume
            
            