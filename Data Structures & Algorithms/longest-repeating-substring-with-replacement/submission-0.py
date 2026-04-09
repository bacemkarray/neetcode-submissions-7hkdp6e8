class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left = 0
        res = defaultdict(int)
        highest_freq = 0
        
        for right in range(len(s)):
            res[s[right]] += 1
            highest_freq = max(highest_freq, res[s[right]])
            
            window_size = right - left + 1
            if window_size - highest_freq > k:
                res[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
        return longest