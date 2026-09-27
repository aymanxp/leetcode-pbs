

# Brute Force method : 
def minCost(cost) : 
    n = len(cost)
    def dfs(i): 
        if i >= n:
            return 0
        return cost[i] + min(dfs(i+1), dfs(i+2))
    return min(dfs(0), dfs(1))


# Memoization method : 
def minCostt(cost): 
    n = len(cost)
    memo = [-1] * n
    def dfs(i):
        if i >= n: 
            return 0 
        if memo[i] != -1: 
            memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
        return memo[i]
    return min(dfs(0), dfs(1))


# Tabulation method : 
def mincosttt(cost):
    n = len(cost)
    dp = [0] * (n+1)


    for i in range(2, n+1): 
        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
    return dp[n]


