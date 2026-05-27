from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''brute force
        for i  in range(len(numbers)):
            for j in range(i,len(numbers)):
                if i != j:
                    if numbers[i]+numbers[j] == target:
                        return [i+1,j+1]
        
        diff_dict = defaultdict(list)
        for index,i in enumerate(numbers):
            diff_dict[target-i]= [index+1,i]
        
        for index,i in enumerate(numbers):
            if target-i in diff_dict:
                return [diff_dict.get(target-i)[0],i+1]
        '''
        left = 0
        right = len(numbers)-1
        while left < right:
            if numbers[left]+numbers[right] == target:
                return [left+1,right+1]
            elif numbers[left]+numbers[right] < target:
                left += 1
            else:
                right -= 1
        return []
