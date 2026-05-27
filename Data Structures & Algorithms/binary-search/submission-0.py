class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        mid = int(l / 2) 
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            for i in range(mid+1,len(nums)):
                if nums[i] == target:
                    return i
        else:
            for i in range(0,mid):
                if nums[i] == target:
                    return i
        return -1