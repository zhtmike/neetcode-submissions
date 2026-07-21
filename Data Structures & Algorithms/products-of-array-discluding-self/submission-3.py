import numpy as np

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = np.cumprod(nums)
        right = np.cumprod(nums[::-1])[::-1]
        
        output = list()
        for i in range(len(nums)):
            if i == 0:
                output.append(right[1])
            elif i == len(nums) - 1:
                output.append(left[-2])
            else:
                output.append(left[i-1] * right[i+1])

        return output

