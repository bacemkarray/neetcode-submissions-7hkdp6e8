class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        # two 1 steps is equal to one 2 step

        # if i am able to go 2 steps:
        res += 3
             
        def climbing(num):
            if num > n:
                return 0
            if num == n:
                return 1
            
            return climbing(num+1) + climbing(num+2)
        
        return climbing(0)
