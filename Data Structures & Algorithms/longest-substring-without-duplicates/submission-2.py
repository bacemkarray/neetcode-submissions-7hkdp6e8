class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        substring = set()
        l = 0

        for r in range(len(s)):
            while s[r] in substring:
                substring.remove(s[l])
                l += 1
            length = r - l + 1
            substring.add(s[r])
            r += 1

            longest = max(longest, length)
        return longest
