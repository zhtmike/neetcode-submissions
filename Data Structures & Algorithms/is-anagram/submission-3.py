from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_cnt = Counter(s)
        t_cnt = Counter(t)
        if s_cnt.keys() != t_cnt.keys():
            return False

        for s, cnt in s_cnt.items():
            if t_cnt[s] != cnt:
                return False

        return True