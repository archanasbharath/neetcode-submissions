class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        brute force
        
        for i in range(0,len(nums)+1):
            if i not in nums:
                return i
        '''
        nums.sort()
        if len(nums) != nums[-1]:
            return len(nums)
        for i in range(0,len(nums)):
            if i != nums[i]:
                return i