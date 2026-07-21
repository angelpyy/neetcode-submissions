class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_set = set()
        
        for i in range(len(nums)):
            if nums[i] in new_set:
                return True
            new_set.add(nums[i])
        return False