# Pattern: Sliding Window
# Time: O(n) | Space: O(m)
# Tripped up on: count occurences in hashmaps and keep track of a have and need variable.
#                store r and l pointers in res and update resLen - storing substring less efficient
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, window = {}, {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have, need = 0, len(countT)
        res = [-1, -1]
        resLen = float("inf")

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                c = s[l]
                window[c] -= 1

                if c in countT and window[c] < countT[c]:
                    have -= 1

                l += 1

        if resLen == float("inf"):
            return ""

        return s[res[0]:res[1] + 1]