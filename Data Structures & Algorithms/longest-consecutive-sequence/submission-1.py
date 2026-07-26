class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        nums_min, nums_max = min(nums), max(nums)
        diff = nums_max - nums_min
        
        unions = list()
        union_set = list()
        for val in range(nums_min, nums_max + 1):
            if val in nums_set:
                union_set.append(val)
            else:
                unions.append(union_set)
                union_set = []

        unions.append(union_set)

        return max([len(x) for x in unions])
