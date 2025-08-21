class solution(object):
    def three_sum(self , nums):

        nums.sort()
        res = []
        
        
        
        n = len(nums)
        for i in range(len(nums)):
            
            if i>0 and nums[i] == nums[i-1]:
                continue

            j , end = i+1 , n-1

            while j < end :
                total = nums[i]+nums[j]+nums[end]
                if total == 0:
                    res.append([nums[i], nums[j], nums[end]])
                    j+=1
                    end-=1


                    while j < end and nums[j] == nums[j-1]:
                        j+=1
                    while j<end and  nums[end] == nums[end+1]:
                        end -=1
                elif total < 0:
                    j+=1
                else:
                    end -=1


        return res   
s = solution()
print(s.three_sum([1,-1,-3,0,0,3]))
            

            

