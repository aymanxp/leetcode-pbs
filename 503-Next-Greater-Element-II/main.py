class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        arr = [[a, i] for i, a in enumerate(nums) ]
        res = [-1] * n
        st = [arr[0]]

        for i in range(1, 2*n) : 
            a, idx = arr[i%n][0], arr[i%n][1]
            while st and a > st[-1][0]: 
                elt = st.pop()
                aSt, idxSt = elt[0], elt[1]
                if res[idxSt] == -1: 
                    res[idxSt] = a 
            st.append(arr[i%n])
        return res



        
