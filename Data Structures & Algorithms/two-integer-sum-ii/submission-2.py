class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        diff_map = defaultdict()

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in diff_map:
                return [diff_map[diff] + 1, i + 1]
            else:
                diff_map[numbers[i]] = i

        # i = 0
        # j = len(numbers) - 1

        # while i < j:
        #     if numbers[i] + numbers[j] < target:
        #         i += 1
        #     elif numbers[i] + numbers[j] > target:
        #         j -= 1
        #     else:
        #         return [i + 1, j + 1]
        