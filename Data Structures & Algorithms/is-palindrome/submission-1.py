class Solution:
    def isPalindrome(self, s: str) -> bool:
        # i = 0
        # j = len(s) - 1
 

        # while i <= j:
        #     if not self.isAlphaNum(s[i]):
        #         i += 1
        #         continue
        #     if not self.isAlphaNum(s[j]):
        #         j -= 1
        #         continue
                
        #     if s[i].lower() != s[j].lower():
        #         return False

        #     i += 1
        #     j -= 1

        # return True
        clean_string = ""

        for char in s:
            if self.isAlphaNum(char):
                clean_string += char

        clean_string = clean_string.lower()
        print(clean_string)
        if clean_string[::-1] == clean_string:
            return True
        
        return False

    def isAlphaNum(self, char:str) -> bool:
        if ord(char) >= 48 and ord(char) <= 57:
            return True
        
        if ord(char) >= 65 and ord(char) <= 90:
            return True

        if ord(char) >= 97 and ord(char) <= 122:
            return True

        return False