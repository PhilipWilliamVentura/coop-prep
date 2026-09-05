# Pattern: HashSet
# Time: O(n) | Space: O(n)
# Tripped up on: turn nums into a set instead of sorting. Lookup becomes O(1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0

        for n in numset:
            if (n-1) not in numset:
                length = 1
                while (n + length) in numset:
                    length += 1
                res = max(length, res)
        return res