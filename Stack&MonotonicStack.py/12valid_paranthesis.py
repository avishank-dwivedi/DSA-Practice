class solution(object):
    def valid_paranthesis(self , s ) :
        stack = []

        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                # If stack is empty, no opening bracket to match
                if not stack:
                    return False
                
                # Check top of stack and current char for a valid match
                top = stack[-1]
                if (top == '(' and char == ')') or \
                   (top == '[' and char == ']') or \
                   (top == '{' and char == '}'):
                    stack.pop()  # Valid match, remove from stack
                else:
                    return False  # Mismatch

        # If stack is empty, all brackets matched properly
        return not stack
    
s = solution()
print(s.valid_paranthesis("{([])"))

