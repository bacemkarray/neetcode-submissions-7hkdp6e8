class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        cache = [-1 for i in range(0, n)]
        cache[0] = 1
        cache[1] = 2
    
        for i in range(2, n):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[n-1]







        # def climbing(num):
        #     if num > n:
        #         return 0
        #     if num == n:
        #         return 1
            
        #     return climbing(num+1) + climbing(num+2)
        
        # return climbing(0)
