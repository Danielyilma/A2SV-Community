class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        result = []
        row = len(mat)
        col = len(mat[0])
        temp = []

        if r * c != col * row:
            return mat
        
        for i in range(row):
            for j in range(col):
                temp.append(mat[i][j])
        
        k = 0
        for i in range(r):
            temp1 = []
            for j in range(c):
                temp1.append(temp[k])
                k += 1
            result.append(temp1)
        return result
                
