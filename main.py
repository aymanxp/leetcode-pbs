

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: 
            return n
        tab = [0] * (n + 1) 
        tab[0], tab[1], tab[2] = 0, 1, 2 
        for i in range(3, n+1):
            tab[i] = tab[i-1] + tab[i-2]
        return tab[n];

