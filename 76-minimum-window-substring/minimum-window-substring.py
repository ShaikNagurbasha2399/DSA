import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        sol = s + s  
        dic = collections.Counter(t)
        required = len(t)
        c = required

        l = 0
        for r in range(len(s)):
            if s[r] in dic:
                dic[s[r]] -= 1
                if dic[s[r]] >= 0:
                    c -= 1

            while c == 0:
                if (r - l + 1) < len(sol):
                    sol = s[l:r+1]

                if s[l] in dic:
                    dic[s[l]] += 1
                    if dic[s[l]] > 0:
                        c += 1
                l += 1

        return sol if sol != s + s else ""





            