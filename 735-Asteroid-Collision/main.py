
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:

        stack = [asteroids[0]]
        for i in range(1, len(asteroids)): 

            if len(stack) > 0 and stack[-1] > 0 and asteroids[i] < 0: 
                equal = False
                while stack: 
                    if stack[-1] > 0 and asteroids[i] < 0 and stack[-1] + asteroids[i] == 0 : 
                        stack.pop()
                        equal = True
                        break
                    elif stack[-1] > 0 and asteroids[i] < 0 and abs(asteroids[i]) > abs(stack[-1]): 
                        stack.pop()
                    elif stack[-1] > 0 and asteroids[i] < 0 and abs(asteroids[i]) < abs(stack[-1]): 
                        break
                    else : 
                        stack.append(asteroids[i])
                        break


                if len(stack) == 0 and not equal: 
                    stack.append(asteroids[i])

            else :
                stack.append(asteroids[i])


        return stack





