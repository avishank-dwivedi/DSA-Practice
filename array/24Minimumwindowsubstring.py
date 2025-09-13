from collections import Counter
class solution(object):
    def minwindow(self , s , t):
        if not t or not s:
            return ""
        
        need = Counter(t)
        window = {}
        have , need_total = 0 , len(need)
        res , res_len = [-1 , -1], float("inf")

        left = 0
        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0)+1

            if ch in need and window[ch] == need[ch]:
                have +=1
            
            while have == need_total:
                if(right - left +1)< res_len:
                    res = [left , right]
                    res_len = right - left +1
                
                window[s[left]] -=1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -=1
                left +=1
        l , r = res
        return s[l:r+1] if res_len != float("inf") else ""