class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = 0
        '''
        for l in range(len(heights)):
            for b in range(l+1,len(heights)):
                area = min(heights[l],heights[b]) * (b-l)
                output = max(output,area)
        return output
        '''
        
        left = 0
        right = len(heights)-1
        while left < right:
            length = right - left
            breadth = min(heights[left],heights[right])
            output = max(output, length*breadth)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return output


        

        