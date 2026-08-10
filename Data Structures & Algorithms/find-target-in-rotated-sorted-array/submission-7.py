class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self._search(nums, target, 0, len(nums) - 1)
        
    def _search(self, nums: List[int], target: int, start: int, end: int):
        pivot = (start + end) // 2

        if nums[pivot] == target:
            return pivot
        elif start == end:
            return -1
        elif end - start == 1:
            if nums[start] == target:
                return start
            elif nums[end] == target:
                return end
            else:
                return -1

        if nums[start] < nums[pivot]:
            if target >= nums[start] and target <= nums[pivot]:
                return self._search(nums, target, start, pivot)
            else:
                return self._search(nums, target, pivot, end)
        else:
            if target >= nums[pivot] and target <= nums[end]:
                return self._search(nums, target, pivot, end)
            else:
                return self._search(nums, target, start, pivot)
