// https://leetcode.com/problems/asteroid-collision

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        while i < len(asteroids):
            if not stack:
                stack.append(asteroids[i])
                i += 1
            else:
                if asteroids[i] < 0 and stack[-1] > 0: #collision
                    if abs(asteroids[i]) == stack[-1]:
                        stack.pop()
                        i += 1
                    elif abs(asteroids[i]) < stack[-1]:
                        i += 1
                    else: # leftward collision
                        stack.pop()
                else:
                    stack.append(asteroids[i])
                    i += 1
        return stack