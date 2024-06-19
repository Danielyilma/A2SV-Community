class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])

        for word in words:
            temp = Counter(word)
            for i in common.keys():
                if i in word:
                    if temp[i] < common[i]:
                        common[i] = temp[i]
                else:
                    common[i] = 0
        res = []
        for key in common:
            while common[key]:
                res.append(key)
                common[key] -= 1
        
        return res
        
