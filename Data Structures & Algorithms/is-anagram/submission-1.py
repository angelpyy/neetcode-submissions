class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # some data struct like hashmap def the best but i dont got it
        # we'll use dictionary
        seen_s, seen_t = {}, {}

        for i in range(len(s)):
            if s[i] not in seen_s:
                seen_s[s[i]] = 0
            seen_s[s[i]] += 1

            if t[i] not in seen_t:
                seen_t[t[i]] = 0
            seen_t[t[i]] += 1

        if seen_s == seen_t:
            return True
        return False