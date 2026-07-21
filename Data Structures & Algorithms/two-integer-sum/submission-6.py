class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs_map = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in pairs_map:
                return [pairs_map[diff], i]

            # we wanna look backward
            pairs_map[nums[i]] = i
            
        return [-1, -1]