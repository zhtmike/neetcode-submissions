from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = Counter(nums).most_common(k)
        cnts = [x for x, _ in cnts]
        return cnts
