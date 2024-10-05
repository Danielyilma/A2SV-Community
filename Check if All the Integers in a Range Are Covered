class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        m_covered = {i for i in range(left, right + 1)}

        for i in range(len(ranges)):
            for j in range(ranges[i][0], ranges[i][1] + 1):
                if j in m_covered:
                    m_covered.remove(j)
                    
        return len(m_covered) == 0
