class Solution:
    def isValid(self, s: str) -> bool:
        partners = {")": "(", "}": "{", "]": "["}
        stack = []
                   
        for char in s:
            if char not in partners:
                stack.append(char)
            else:
                if stack and stack[-1] == partners[char]:
                    stack.pop()
                else:
                    return False 
            
        return True if not stack else False