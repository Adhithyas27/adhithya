class Solution:
    def isMatch(self, s, p):
        matches = [[False for j in range(len(s) + 1)] for i in range(len(p) + 1)]
        matches[0][0] = True
        for i in range(2, len(p) + 1):
            if p[i - 1] == "*": 
                matches[i][0] = matches[i - 2][0]
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i -1] == s[j - 1] or p[i - 1] == ".":
                    matches[i][j] = matches[i - 1][j - 1]
                elif p[i - 1] == "*": 
                    if p[i - 2] != s[j - 1] and p[i - 2] != ".":
                        matches[i][j] = matches[i - 2][j]
                    else:
                        matches[i][j] = matches[i - 2][j] or matches[i -1][j] or matches[i][j - 1] 
        return matches[-1][-1]
