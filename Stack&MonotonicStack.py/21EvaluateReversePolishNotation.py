class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token not in "+-*/":  # check all 4 operators
                stack.append(int(token))
            else:
                num1 = stack.pop()  # right operand
                num2 = stack.pop()  # left operand
                if token == '+':
                    stack.append(num2 + num1)
                elif token == '-':
                    stack.append(num2 - num1)
                elif token == '*':
                    stack.append(num2 * num1)
                elif token == '/':
                    stack.append(int(float(num2) / num1))  # truncate towards zero
        return stack[0]
s = Solution()
print(s.evalRPN["2","1","+","3","*"])