class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = 0
        for l in range(len(heights)):
            for b in range(l+1,len(heights)):
                area = min(heights[l],heights[b]) * (b-l)
                output = max(output,area)
        return output

        