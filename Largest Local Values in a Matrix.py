class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rowlen = len(grid) - 2
        result = []

        for i in range(rowlen):
            temp = []
            for j in range(rowlen):
                max1 = max(grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3])
                 
                temp.append(max1)
            result.append(temp)
        return result
