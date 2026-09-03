# Pattern: Store length + delimeter before each string
# Time: O(m+n) | Space: O(m+n)
# Tripped up on: length of string could be more then one character. Delimeter comes after length.
class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs:
            ans += (str(len(word)) + "#" + word)
        return ans
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i != len(s):
            j = i
            while s[j] != "#":
                j+= 1
            length = int(s[i:j])
            i = j+length+1
            ans.append(s[j+1:i])
        return ans