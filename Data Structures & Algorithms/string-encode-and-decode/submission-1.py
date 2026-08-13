class Solution:

    def encode(self, strs: List[str]) -> str:
        # count the length of each word in the array and save them..
        word_lens = []
        for word in strs:
            word_lens.append(len(word))

        # [Hello, World] [5, 5]
        encoded = ""
        for i in range(len(strs)):
            encoded += f"{word_lens[i]}#{strs[i]}" # "5#Hello"
        
        return encoded # "5#Hello5#World"


    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            # start only looking at len: LEN CAN BE MORE THAN ONE DIGIT
            j = i 
            while j < len(s) and s[j] != '#':
                j += 1

            # slice length out and convert resulting string to int
            length = int(s[i:j])

            # we have start (i) length and end is the sum and we reset i
            word = s[j+1:j+length+1]
            strs.append(word)

            # new i
            i = j + length + 1 # also skip over the delim

        return strs



