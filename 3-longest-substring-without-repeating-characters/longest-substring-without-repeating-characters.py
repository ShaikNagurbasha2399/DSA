class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        s = [i for i in s]
        lst = []
        l = 0
        r = 1
        while r <= len(s):
            if len(s[l:r]) == len(set(s[l:r])):
                r += 1
            else:
                lst.append(len(s[l:r-1])) 
                l += 1
            if l >= r:
                r += 1
        lst.append(len(s[l:r-1]))
        return max(lst)