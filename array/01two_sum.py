class Solution(object):
    def twosum(self , nums ,target):
        
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                if nums[i] + nums[j] == target:
                    return [i , j]
ts =Solution()
print(ts.twosum([2,3,4,5] , 7))
        