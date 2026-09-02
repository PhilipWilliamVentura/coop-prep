# Pattern: Hashmaps
# Time: O(n+m) | Space: O(1)
# Tripped up on: straight forward problem
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictionary_s = {}
        dictionary_t = {}

        for i in range(len(s)):
            dictionary_s[s[i]] = dictionary_s.get(s[i], 0) + 1
            dictionary_t[t[i]] = dictionary_t.get(t[i], 0) + 1
        
        return dictionary_s == dictionary_t