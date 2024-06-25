class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if matrix[0][0] > target:
            return False

        for i in range(len(matrix)):
            if matrix[i][0] < target and matrix[i][0] > target:
                continue
            
            j, k = 0, len(matrix[i]) - 1

            while j <= k:
                mid = (j + k) // 2

                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    k = mid - 1
                else:
                    j = mid + 1
        
