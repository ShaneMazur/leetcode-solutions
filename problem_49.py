'''
Problem:
Given an array of strings, group anagrams together.

Ex.
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

'''
from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for s in strs:
            found = False
            cs = Counter(s)
            for k in d.keys():
                if cs == d[k][0]:
                    d[k][1].append(s)
                    found = True
                    break
            if not found:
                d[s] = [cs,[s]]
        return [v[1] for v  in d.values()]
