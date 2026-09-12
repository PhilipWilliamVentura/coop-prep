# Pattern: Sliding Window
# Time: O(n) | Space: O(m)
# Tripped up on: Count occurence of chars using a hashmap
#                use a variable to keep track of max frequency and you don't have to lower it when moving the window 
#                because the result won't change unless it gets higher
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = {}
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])
            while k < r - l + 1 - maxf:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res