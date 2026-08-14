class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)

        for i in range(len(height)):
            if i == 0:
                max_left[i] = 0
                continue
            
            if max_left[i - 1] >= height[i - 1]:
                max_left[i] = max_left[i - 1]
            else:
                max_left[i] = height[i - 1]

        for i in range(len(height) - 1, -1,-1):
            if i == len(height) - 1:
                max_right[i] = 0
                continue

            if max_right[i + 1] >= height[i + 1]:
                max_right[i] = max_right[i + 1]
            else:
                max_right[i] = height[i + 1]

        res = 0
        for i in range(len(height)):
            trapped = min(max_left[i], max_right[i]) - height[i]

            if trapped > 0:
                res += trapped

        return res