class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d={}
        result = []

        for i in strs:
            if str(sorted(i)) in d:
                d[str(sorted(i))].append(i)
            else:
                d[str(sorted(i))]=[i]

        for i in d:
            result.append(d[i])

        return result
