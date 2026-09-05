# Pattern: Two pointers
# Time: O(n) | Space: O(1)
# Tripped up on: straight forward problem
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()
        while l < r:
            while l<r and not self.is_alpha_num(s[l]):
                l += 1
            while l<r and not self.is_alpha_num(s[r]):
                r -= 1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def is_alpha_num(self, c: str) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))