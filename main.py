


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        cache = [-1] * n 

        def dfs(i): 
            if i >= n: 
                return 0
            if cache[i] == -1:
                cache[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return cache[i]
        return min(dfs(0), dfs(1))


