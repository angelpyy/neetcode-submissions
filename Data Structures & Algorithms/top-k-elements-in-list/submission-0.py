class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        # first we need to count
        for i in nums:
            count[i] += 1

        # sorted solution, sort on value in descending order
        sorted_count = sorted(count.items(), key=lambda pair: pair[1], reverse=True)
        
        # slice to only k elements
        top_k = sorted_count[:k]

        # return only the key which is the actual number not count
        return [pair[0] for pair in top_k]

        # we now have a dict that tells us how many times something appears
        # bucket sort? 
        # frequency = [[]] * len(nums)

        # loop thrugh 
        # for key in count:
        #     frequency

