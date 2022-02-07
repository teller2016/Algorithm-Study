#https://leetcode.com/problems/group-anagrams/submissions/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = collections.defaultdict(list)
        for w in strs:
            anagram[''.join(sorted(w))].append(w)
        return anagram.values()