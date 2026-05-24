class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Brute force
        '''

        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

        #for index,val in enumerate(nums):
        #    if target - val 
            
        