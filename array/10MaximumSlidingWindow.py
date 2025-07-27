class solution(object):
    def MaximumSlidingWindow(self , nums , K):

        max_K = []
        for i in range(len(nums) - K+1):
            window = nums[i:i+K]
            max_K.append(max(window))
        return max_K
    
s = solution()
print(s.MaximumSlidingWindow([1,-2,-3,4,5,-5,4,8,-4] , 3))