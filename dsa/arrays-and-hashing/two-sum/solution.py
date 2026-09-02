# Pattern: Hashmaps
# Time: O(n) | Space: O(n)
# Tripped up on: keys are the numbers and values are the indices
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for ind, val in enumerate(nums):
            diff = target - val
            if diff in hashmap:
                return [hashmap[diff], ind]
            else:
                hashmap[val] = ind