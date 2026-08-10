class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        pivot = len(nums) // 2
        left = nums[:pivot]
        right = nums[pivot:]
        if left[-1] > right[-1]:
            return self.findMin(right)
        else:
            return self.findMin(left)
        