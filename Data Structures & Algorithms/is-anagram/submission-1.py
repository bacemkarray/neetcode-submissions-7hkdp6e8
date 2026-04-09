class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # put string s into a hashmap where char is key and value is frequency
        if len(s) != len(t):
            return False
        
        s_dict = {}
        t_dict = {}
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        
        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1
        
        for char in s_dict:
            if s_dict[char] != t_dict.get(char, 0):
                return False
        return True

        