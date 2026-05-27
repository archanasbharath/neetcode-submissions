class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            print(i,i+k)
            if i+k < len(nums)+1:
                output.append(max(nums[i:i+k]))
        return output

            
        