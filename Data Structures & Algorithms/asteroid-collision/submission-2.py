class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            alive = True
            size = abs(asteroid)
            while stack and alive and asteroid < 0 and stack[-1] > 0:
                if stack[-1] == size:
                    stack.pop()
                    alive = False
                elif stack[-1] < size:
                    stack.pop()
                else:
                    alive = False
            if alive:
                stack.append(asteroid)
        return stack