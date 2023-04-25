from typing import List
import collections 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ans = collections.defaultdict(list)
        # for s in strs:
        #     ans[tuple(sorted(s))].append(s)
        # return ans.values()
        d = collections.defaultdict(list)
        for s in strs:
            s2 = ''.join(sorted(s))
            d[tuple(sorted(s))].append(s)
        ans = []
        for l in d:
            ans.append(d[l])

        return ans
    
strs = ["eat","tea","tan","ate","nat","bat"]
# strs = [""]
# strs = ["a"]

print(Solution.groupAnagrams(Solution, strs))