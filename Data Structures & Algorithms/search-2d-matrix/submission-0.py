class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = (len(matrix) * len(matrix[0])) - 1

        while left <= right:

            mid = (left + right) // 2
            rows = mid // len(matrix[0])
            cols = mid % len(matrix[0])

            if target == matrix[rows][cols]:
                return True

            if target > matrix[rows][cols]:
                left = mid + 1
            
            if target < matrix[rows][cols]:
                right -= 1
            
        
        return False






        
