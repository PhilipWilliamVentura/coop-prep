# Pattern: Bucket Sort
# Time: O(n) | Space: O(n)
# Tripping up on: number of buckets cannot be greater than length of nums, 
#                 .items() similar to .enumerate() but for dicts
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums))]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt-1].append(num)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res