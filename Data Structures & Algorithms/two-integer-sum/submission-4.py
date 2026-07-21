class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs_map = {}

        for i in range(len(nums)):
            pair = target - nums[i]

            if pair in pairs_map:
                return [pairs_map[pair], i]

            # we wanna look forward
            pairs_map[nums[i]] = i
            
        return [-1, -1]