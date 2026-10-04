
## Three pointers 
class Solution:
    def sortColors(self, nums): 
        def swap(i, j): 
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        l, r = 0, len(nums) - 1
        i = 0
        while i <= r: 
            if nums[i] == 0: 
                swap(l, i)
                l += 1
            elif nums[i] == 2: 
                swap(r, i)
                r -= 1
                i -= 1
            i += 1






## Using bubble sort 
class Solution2:
    def sortColors(self, nums: list[int]) -> None:
        n = len(nums)
        for i in range(n-1): 
            for j in range(n-i-1): 
                if nums[j] > nums[j+1]: 
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        
