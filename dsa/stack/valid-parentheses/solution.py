# Pattern: Stack
# Time: O(n) | Space: O(n)
# Tripped up on: straight forward problem
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stack = []
        for bracket in s:
            if bracket in dic:
                if not stack or stack.pop() != dic[bracket]:
                    return False
            else:
                stack.append(bracket)
        return not stack

            