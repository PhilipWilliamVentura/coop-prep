# Pattern: Sliding Window
# Time: O(n) | Space: O(m)
# Tripped up on: Search in hashmap or set for O(1) lookup
#                Update left pointer to the first of duplicates if still in window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        res = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
            r += 1
        return res