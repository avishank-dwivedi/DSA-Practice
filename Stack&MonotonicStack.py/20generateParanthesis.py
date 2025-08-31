class Solution(object):
    def backtrack(self , n):
        res = []
        def backtrack(curr , open_curr , close_curr):
            if len(curr) == 2*n:
                res.append(curr)
                return
            if open_curr < n:
                backtrack(curr + "(", open_curr+1 , close_curr)
            if close_curr < open_curr:
                backtrack(curr + ")" , open_curr , close_curr + 1)
        backtrack("" , 0 , 0)
        return res
s = Solution()
print(s.backtrack(3))