class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_set = dict(zip(nums, range(len(nums))))
        
        triplets = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                k_num = 0 - nums[i] - nums[j]
                if k_num in nums_set and nums_set[k_num] not in (i, j):
                    triplets.append([nums[i], nums[j], k_num])

        # O(C x N) sorting 
        triplets = [tuple(sorted(x)) for x in triplets]
        triplets = set(triplets)
        triplets = [list(x) for x in triplets]

        return triplets
