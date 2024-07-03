class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        inc = False
        dec = False

        for i in range(1, len(arr)):
            if not dec and arr[i - 1] < arr[i]:
                inc = True
            elif inc and arr[i - 1] > arr[i]:
                dec = True
            else:
                dec = False
                break
        
        return inc and dec
