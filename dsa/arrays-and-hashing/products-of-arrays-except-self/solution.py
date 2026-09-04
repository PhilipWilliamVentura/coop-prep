# Pattern: Prefix/Suffix
# Time: O(n) | Space: O(n)
# Tripped up on: Don't have to store prefix and suffix in different arrays, fill res with 1s multiply them with the prefix and a second pass with the suffix
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res