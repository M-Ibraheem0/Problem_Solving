class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            flag = True
            while len(stack) and flag and asteroid < 0 and stack[-1] > 0:
                if stack[-1] == abs(asteroid):
                    stack.pop()
                    flag = False
                elif stack[-1] < abs(asteroid):
                    stack.pop()
                else:
                    flag = False
            if flag:
                stack.append(asteroid)
        return stack