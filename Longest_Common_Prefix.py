class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            if i >= len(strs[0]):
                break
            temp = strs[0][i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]):
                    return res

                if temp != strs[j][i]:
                    return res
            res += temp
        return res
