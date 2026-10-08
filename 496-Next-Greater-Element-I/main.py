
## Monotonic stack approach 

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = [-1] * len(nums1)
        mp = {num: i for i, num in enumerate(nums1)}
        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]: 
                val = stack.pop()
                idx = mp[val]
                res[idx] = cur
            if cur in mp:
                stack.append(cur)
        return res
        
