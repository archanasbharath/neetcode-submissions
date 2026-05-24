class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        brute force
        '''
        output = []
        if len(set(nums)) == 1:
            if nums[0] == 0:
                return nums
            
        for i in range(0,len(nums)):
            prdt = 1
            for j in range(0,len(nums)):
                if i != j:
                    prdt *= nums[j]
            output.append(prdt)
        return output


        