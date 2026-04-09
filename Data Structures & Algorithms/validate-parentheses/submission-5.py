class Solution:
    def isValid(self, s: str) -> bool:
        partners = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in partners:
                if stack and stack[-1] == partners[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False            
