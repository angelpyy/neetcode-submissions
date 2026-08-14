class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(':')', '{':'}', '[':']'}

        for char in s:
            if char in pairs:
                # check for opening bracket; add to stack
                stack.append(char)
            else:
                # closing bracket; stack pop must return the corresponding opening
                if not stack or pairs[stack.pop()] != char:
                    return False

        return len(stack) == 0