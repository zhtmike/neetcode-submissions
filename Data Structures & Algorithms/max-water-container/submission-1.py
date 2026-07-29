class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1

        areas = list()
        
        while j > i:
            area = min(heights[i], heights[j]) * (j - i)
            areas.append(area)

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return max(areas)
