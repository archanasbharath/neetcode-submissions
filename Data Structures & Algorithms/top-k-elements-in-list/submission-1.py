from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1 or len(set(nums)) == 1:
            return list(set(nums))
        cnt_dict = Counter(nums)
        outp = []
        for kk,vv in cnt_dict.items():
            heapq.heappush(outp,(vv,kk))
            if len(outp) > k:
                heapq.heappop(outp)
        return[x[1] for x in outp]
        