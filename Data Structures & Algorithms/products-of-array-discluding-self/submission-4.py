class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        # Build left products IN the result array
        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]
        
        # Build right products and multiply as you go
        right = 1
        for i in range(n - 1, -1, -1):
            result[i] = result[i] * right
            right *= nums[i]
        
        return result