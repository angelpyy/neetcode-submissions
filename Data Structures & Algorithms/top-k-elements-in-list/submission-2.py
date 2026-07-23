class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        # first we need to count
        # k = number; v = apperances ex: (7, 2)
        for i in nums:
            count[i] += 1

        frequency = [[] for i in range(len(nums) + 1)]
        for num, freq in count.items():
            frequency[freq].append(num)

        result = []
        for count_value in range(len(frequency) - 1, 0, -1):
            for num in frequency[count_value]:
                result.append(num)
                if len(result) == k:
                    return result

        return result