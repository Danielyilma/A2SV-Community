class Solution:
    def interpret(self, command: str) -> str:
        Gmap = {"()" : "o", "(al)": "al"}
        res = ""

        i = 0
        while i < (len(command)):
            if command[i] == "(":
                temp = ""
                while command[i] != ")":
                    temp += command[i]
                    i += 1
                temp += ")"
                res += Gmap[temp]
            else:
                res += command[i]
            i += 1
        return res
