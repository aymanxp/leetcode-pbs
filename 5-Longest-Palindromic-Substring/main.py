

# Brute force 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res, resLen = "", 0

        for i in range(n): 
            for j in range(i, n): 
                l, r = i, j 
                while l < r and s[l] == s[r]: 
                    l += 1 
                    r -= 1 
                if l >= r and j - i + 1 > resLen: 
                    res = s[i:j+1] 
                    resLen = j - i + 1
        return res 


# DP Buttom up  
class Solution1: 
    def longestPalindrome(self, s: str) -> str: 
        n:int = len(s)
        resIdx, resLen = 0, 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1): 
            for j in range(i, n): 
                if s[i] == s[j] and (j - i + 1 <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True 
                    if resLen < j - i + 1: 
                        resIdx = i
                        resLen = j - i + 1 
        return s[resIdx: resIdx+resLen]


class Solution2: 
    def longestPalindrome(self, s: str) -> str: 
        n: int = len(s)
        resIdx, resLen = 0, 0 
        for i in range(n): 
            # Odd length 
            l, r = i, i 
            while l >= 0 and r < n and s[l] == s[r]: 
                if r - l + 1 > resLen: 
                    resLen = r - l + 1 
                    resIdx = l 
                l -= 1 
                r += 1 
            # Even length 
            l, r = i, i+1 
            while l >= 0 and r < n and s[l] == s[r]: 
                if r - l + 1 > resLen: 
                    resLen = r - l + 1 
                    resIdx = l 
                l -= 1 
                r += 1 

        return s[resIdx: resIdx+resLen]


