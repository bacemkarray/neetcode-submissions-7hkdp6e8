class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        def convert(num):
            ones = 0
            while num >= 1:
                rem = num % 2
                if rem: 
                    ones += 1
                num //= 2
            return ones

        for i in range(0, n+1):
            res.append(convert(i))

        return res