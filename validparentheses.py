class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range (0, len(s)):
            if s[i] == "(":
                stack.append(s[i])
            if s[i] == "[":
                stack.append(s[i])
            if s[i] == "{":
                stack.append(s[i])

            if not stack:
                return False
            top_element = stack[-1]
            
            if s[i] == ")": 
                if top_element == "(":
                    stack.pop()
                else: 
                    return False
            if s[i] == "]": 
                if top_element == "[":
                    stack.pop()
                else: 
                    return False
            if s[i] == "}": 
                if top_element == "{":
                    stack.pop()
                else: 
                    return False
        
        return not stack

# essentially, it goes char by char and pushes the opening of the brackets into the stack. once it gets to a closing bracket, the corresponding opening bracket should the curr at the top of the stack, if not -> out of order so return false. should have an empty stack at the end bc everything will be popped out
            

                 
        