class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        dic = {}
        max = -1
        for i in range(len(arr) - 1, -1, -1):
            dic[i] = max
            if max < arr[i]:
                max = arr[i]
        
        for i in range(len(arr)):
            arr[i] = dic[i]
        return arr
