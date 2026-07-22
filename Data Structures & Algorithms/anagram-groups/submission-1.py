class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for anagram in strs:
            count = [0]*26

            # find their 'total'
            for char in anagram:
                count[ord(char) - ord('a')] += 1
            
            if tuple(count) not in anagrams:
                anagrams[tuple(count)] = []
            anagrams[tuple(count)].append(anagram)

        return list(anagrams.values())
