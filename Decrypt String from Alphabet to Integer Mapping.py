class Solution:
    def freqAlphabets(self, s: str) -> str:
        letters = "abcdefghijklmnopqrstuvwxyz"
        dec_key = {}
        res = ""

        dec_key = {str(i) if i < 10 else str(i) + "#": letters[i - 1] for i in range(1, len(letters) + 1)}

        i = 0
        while i < (len(s)):
            if i + 2 < len(s) and s[i + 2] == "#":
                res += dec_key[s[i:i+3]]
                i += 2
            else:
                res += dec_key.get(s[i], "")
                pass
            i += 1

        return res
