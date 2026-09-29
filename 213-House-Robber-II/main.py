
# Memoization 
class Solution: 
    def rob(self, nums) : 
        if len(nums) == 1: 
            return nums[0]
        memo = [[-1] * 2 for _ in range(len(nums))]

        def dfs(i, flag): 
            if i >= len(nums) or (flag and i == len(nums) - 1): 
                return 0 
            if memo[i][flag] == -1: 
                memo[i][flag] = max(dfs(i+1, flag), nums[i] + dfs(i + 2, flag or (i == 0)))
            return memo[i][flag]
        return max(dfs(0, True), dfs(1, False))



 



# Tabulation 
class Solution2:
    def rob(self, nums: list[int]) -> int:
        if not nums: 
            return 0 
        if len(nums) == 1: 
            return nums[0]
        if len(nums) == 2: 
            return max(nums[0], nums[1])
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums): 
        n = len(nums)
        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n): 
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[-1]

# Tabulation space optimized 

class Solution3: 
    def rob(self, nums): 
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums): 
        rob1 = 0 
        rob2 = 0 
        for num in nums: 
            newRob = max(rob1 + num, rob2)
            rob1 = rob2 
            rob2 = newRob
        return rob2
