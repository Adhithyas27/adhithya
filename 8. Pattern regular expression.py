class Solution(object):
    def isMatch(self, s, p):
        res = [[False for x in range(len(p) + 1)] for y in range(len(s) + 1)]
        res[0][0] = True

        for j in range(1, len(p) + 1):
            if p[j - 1] == "*":
                res[0][j] = res[0][j - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == ".":
                    res[i][j] = res[i - 1][j - 1]
                if p[j - 1] == "*":
                    res[i][j] = res[i][j - 2]  
                    if p[j - 2] == s[i - 1] or p[j - 2] == ".":
                        res[i][j] = res[i][j - 2] or res[i - 1][j]


        return res[-1][-1]
print(isMatch(self,s,p))
