class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        
        col = len(strs[0])
        row = len(strs)

        for i in range(col):
            for j in range(1, row):
                if strs[j - 1][i] > strs[j][i]:
                    count += 1
                    break

        return count
