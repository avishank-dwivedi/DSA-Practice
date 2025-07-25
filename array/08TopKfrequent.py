from collections import Counter
import heapq
class Solution(object):
    def topkfrequency(self , nums , K):
        count = Counter(nums)

        return [items for items, freq in heapq.nlargest(K,count.items(), key=lambda x: x[1])]

ss = Solution()
print(ss.topkfrequency([1,3,1,2,3,4], 2))