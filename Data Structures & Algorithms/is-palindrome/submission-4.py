class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = []
        for char in s:
            if char.isalnum():
                clean_str.append(char.lower())
                
        index_1 = 0
        index_2 = len(clean_str)-1

        while index_1 < index_2:
            if clean_str[index_1] != clean_str[index_2]:
                return False
            index_1 += 1
            index_2 -= 1
        
        return True
