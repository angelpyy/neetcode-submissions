class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_set = set(nums)
        
        
        if len(new_set) == len(nums):
            return False
        return True