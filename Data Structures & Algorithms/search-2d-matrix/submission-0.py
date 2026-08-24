class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left,right = 0,len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_left,mid_right = 0,len(matrix[mid]) - 1
            if target < matrix[mid][mid_left]:
                right = mid - 1
            elif target > matrix[mid][mid_right]:
                left = mid + 1
            else:
                while mid_left <= mid_right:
                    mid_mid = (mid_left + mid_right) // 2
                    if matrix[mid][mid_mid] == target:
                        return True
                    elif matrix[mid][mid_mid] < target:
                        mid_left = mid_mid + 1
                    else:
                        mid_right = mid_mid - 1
                return False
        return False