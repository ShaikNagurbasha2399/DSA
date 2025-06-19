class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        maxCount, left = 0, 0
        longest = 0
        for right, ch in enumerate(s):
            idx = ord(ch) - ord('A')
            counts[idx] += 1
            maxCount = max(maxCount, counts[idx])
            while (right - left + 1) - maxCount > k:
                counts[ord(s[left]) - ord('A')] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest