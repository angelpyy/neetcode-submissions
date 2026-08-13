class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []

        # pointer array method?
        left = []
        right = [1]* len(nums)

        # create left array
        for i in range(len(nums)):
            if i == 0:
                # nothing to the left
                left.append(1)
            else:
                left.append(left[i - 1] * nums[i - 1])

        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            results.append(left[i] * right[i])

        return results