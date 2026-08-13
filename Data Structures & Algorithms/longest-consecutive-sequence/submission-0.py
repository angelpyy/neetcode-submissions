class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        max_length = 0
        for num in num_set:
            if num - 1 in num_set:
                continue
            else:
                length = 1
                i = 1
                while True:
                    if num + i in num_set:
                        length += 1
                        i += 1
                    else:
                        break
                if length > max_length:
                    max_length = length
        
        return max_length
