class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # dictionary method ?
        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = 1 # mark as true exists
        return False



        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False