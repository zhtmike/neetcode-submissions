from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_cnts = [Counter(x) for x in strs]
        
        cnt_dict = defaultdict(list)
        for cnt, s in zip(str_cnts, strs):
            cnt_dict[tuple(sorted(cnt.items()))].append(s)
        
        return list(cnt_dict.values())