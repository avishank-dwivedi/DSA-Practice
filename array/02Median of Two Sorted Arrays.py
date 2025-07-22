class solution(object):
    def findmediansortarray(self,num1,num2):
        merged = sorted(num1 + num2)
        n = len(merged)
        mid = n//2

        if  n%2 == 0:
            return(merged[mid-1] + merged[mid]) / 2.0
        else:
            return float(merged[mid])

median = solution()
print(median.findmediansortarray([1,2,3],[2,3,4]))    
