

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        reminder = {0 : -1}
        total = 0
        for j, num in enumerate(nums):
            total += num 
            r = total % k 
            if r in reminder: 
                if j - reminder[r] >= 2: 
                    return True 
            else:
                reminder[r] = j
        return False
