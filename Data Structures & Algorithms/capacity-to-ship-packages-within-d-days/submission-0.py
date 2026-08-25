class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left,right = max(weights),sum(weights)
        print(right)
        while left <= right:
            total_days,mid = days,(left + right) // 2
            real_val = mid
            for weight in weights:
                if real_val - weight < 0:
                    total_days -= 1
                    real_val = mid
                real_val -= weight
            total_days -= 1
            if total_days >= 0:
                right = mid - 1
            else:
                left = mid + 1
        return left
