class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        brute force
        
        for i in range(0,len(nums)+1):
            if i not in nums:
                return i
        '''
        '''
        nlogn
        nums.sort()
            
        for i in range(0,len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
        '''
        seen = set(nums)
        for i in range(0,len(nums)+1):
            if i not in seen:
                return i