class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_length = 0
        res_index = 0
        def helper(left, right):
            nonlocal res_length, res_index
            l,r = left,right
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > res_length:
                    res_length = r-l+1
                    res_index = l
                l -= 1
                r += 1
        for i in range(len(s)):
            helper(i,i)
            helper(i,i+1)




        return s[res_index:res_length+res_index]