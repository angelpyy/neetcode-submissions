class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero = 0
        for num in nums:
            if num != 0:
                product *= num
            if num == 0:
                zero += 1

        results = []
        for num in nums:
            if zero >= 2:
                results.append(0)
            elif zero and num != 0:
                results.append(0)
            elif zero and num == 0:
                results.append(product)
            else:
                results.append(product // num)
            
        return results