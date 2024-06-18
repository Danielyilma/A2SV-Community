class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = 0
        y = x

        if x < 0:
            return False

        while y:
            res = res * 10 + (y % 10)
            y //= 10
        
        return res == x
