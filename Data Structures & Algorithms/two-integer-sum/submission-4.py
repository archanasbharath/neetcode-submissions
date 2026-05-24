from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Brute force 1
        

        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        '''
        '''
        optimal 1
        
        ss = defaultdict(int)
        for index,val in enumerate(nums):
            ss[val] = index
        for index,val in enumerate(nums):
            if target - val in ss:
                return [min(index,ss[val]),max(index,ss[val])]
        '''
        new_nums = []
        for index,val in enumerate(nums):
            new_nums.append([val,index])

        nums = sorted(new_nums)
        left = 0
        right = len(nums)-1
        while left < right:
            if nums[left][0]+nums[right][0] == target:
                return [min(nums[left][1],nums[right][1]),max(nums[left][1],nums[right][1])]
            elif nums[left][0]+nums[right][0] < target:
                left += 1
            else:
                right -= 1
        return []
        
            
        