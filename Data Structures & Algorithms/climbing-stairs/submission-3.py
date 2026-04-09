class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        cache = [-1 for i in range(0, n+1)]
        cache[1] = 1
        cache[2] = 2
    
        for i in range(3, n+1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[n]







        # def climbing(num):
        #     if num > n:
        #         return 0
        #     if num == n:
        #         return 1
            
        #     return climbing(num+1) + climbing(num+2)
        
        # return climbing(0)
