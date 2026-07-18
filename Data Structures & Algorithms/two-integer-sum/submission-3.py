class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        # build the hash map
        num_dict = dict(zip(nums, range(len(nums))))
        
        # scan all nums
        for i, x in enumerate(nums):
            diff = target - x
            j = num_dict.get(diff, None)
            if j and j != i:
                result.extend((i, j))

        result = list(set(result))
        return result



            
        