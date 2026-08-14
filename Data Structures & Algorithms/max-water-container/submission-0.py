class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = 0

        l = 0
        r = len(heights) - 1
        while l < r:
            width = r - l
            height = min(heights[r],heights[l])

            v = width * height

            if v > volume:
                volume  = v
            
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                if heights[l+1] > heights[r-1]:
                    l += 1
                else:
                    r -= 1
        
        return volume
            
            