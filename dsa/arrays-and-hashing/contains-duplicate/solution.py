# Pattern: Hash Sets
# Time: O(n) | Space: O(n)
# Tripped up on: straight forward problem
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)