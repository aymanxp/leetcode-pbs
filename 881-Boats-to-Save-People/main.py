


class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        cnt = 0
        l, r = 0, len(people) - 1
        while l <= r: 
            if people[l] + people[r] <= limit: 
                cnt += 1
                l += 1 
                r -= 1
            else:
                r -= 1
        return len(people) - cnt


