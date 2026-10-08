# Pattern: Bactracking using dfs
# Time: O(2^(t/m)) | Space: O(t/m) where t is the given total and m the minimum num in nums
# Tripped up on: Two cases: add the same num to list or remove it from the combination and add nothing to the list.

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)
        return res
