class solution(object):
    def next_greater_element(self , nums1 , nums2):
        next_greater = {}
        stack = []

        for i in reversed(nums2):
            while stack and stack[-1] <= i:
                stack.pop()
        
            if stack:
                next_greater[i] = stack[-1]
            else:
                next_greater[i] = -1
            stack.append(i)
    
        result = [next_greater[i] for i in nums1]
        return result

s  = solution()
print(s.next_greater_element(nums1=[4,1,2] , nums2=[1,3,4,2]))