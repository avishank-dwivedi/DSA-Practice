class solution(object):
    def maxsumarray(self,nums):
        global_max = nums[0]
        local_max = nums[0]

        for i in range(1 , len(nums)):
            local_max = max(nums[i] , local_max + nums[i])
            global_max = max(global_max , local_max)

        return global_max
    
ss= solution()
print(ss.maxsumarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))