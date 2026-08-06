class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []

        # sort the array to the do the pointer thing
        nums.sort()

        # loop 
        for i in range(len(nums) - 1):
            # i = i jaja
            left = i + 1
            right = len(nums) - 1

            while (left < right):

                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    triplet = [nums[i], nums[left], nums[right]]
                    if triplet not in results:
                        results.append([nums[i], nums[left], nums[right]])
                    left += 1
                elif sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1

        return results
