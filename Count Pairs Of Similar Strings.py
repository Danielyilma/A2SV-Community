class Solution:
    def similarPairs(self, words: List[str]) -> int:
        arr_set = []
        count = []
        pair = 0

        for word in words:
            tem = set(word)
    
            if tem not in arr_set:
                arr_set.append(tem)
                count.append(1)
            else:
                x = arr_set.index(tem)
                pair += count[x]
                count[x] += 1

        return pair
