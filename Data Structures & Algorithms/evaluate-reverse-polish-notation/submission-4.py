class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for op in tokens:
            if op in operators:
                # else we are an operator and we must operate
                y = int(stack.pop())
                x = int(stack.pop())

                match op:
                    case '+':
                        stack.append(x+y)
                    case '-':
                        stack.append(x-y)
                    case '*':
                        stack.append(x*y)
                    case '/':
                        stack.append(x/y)
            else:
                stack.append(op)
        
        return int(stack.pop())
                        

