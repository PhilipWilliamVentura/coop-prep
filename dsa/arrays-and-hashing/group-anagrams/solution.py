# Pattern: Hashmap
# Time: O(n * m) | Space: O(n * m)
# Tripped up on: python keys must be immutable so we need to transform list into tuple
#                .append() adds a single item to the end of a list while += operator unpacks an iterable and appends all its individual items
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for word in strs:
            count = [0] * 26
            for chars in word:
                count[ord(chars) - ord("a")] += 1
            dic[tuple(count)].append(word)
        return list(dic.values())