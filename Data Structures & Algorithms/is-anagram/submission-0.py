class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # some data struct like hashmap def the best but i dont got it
        # we'll use dictionary
        seen_s = {}
        seen_t = {}
        for letter in s:
            if letter not in seen_s:
                seen_s[letter] = 0
            seen_s[letter] += 1

        for letter in t:
            if letter not in seen_t:
                seen_t[letter] = 0
            seen_t[letter] += 1


        if seen_s == seen_t:
            return True
        return False