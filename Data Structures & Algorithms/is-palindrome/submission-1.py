class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = []
        for char in s:
            if char.isalnum():
                clean_str.append(char.lower())
                
        
        halfway = len(clean_str)//2
        index_1 = 0
        index_2 = len(clean_str)-1

        for i in range(0, halfway):
            if clean_str[index_1+i] != clean_str[index_2-i]:
                return False
        
        return True
