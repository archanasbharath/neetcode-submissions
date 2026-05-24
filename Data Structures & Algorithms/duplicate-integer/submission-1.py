class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        brute force
        
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
        '''
        '''
        Optimal 1
        
        seen = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                return True
        return False
        '''
        '''
        Optimal 2
        '''
        if len(set(nums)) == len(nums):
            return False
        return True
        