class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        
        len_p = len(p)
        len_s = len(s)
        result = []

        if len_p > len_s:
            return []
         
        counter_p = Counter(p)
        window = Counter()

        for i in range(len_s):
            window[s[i - len_s]] += 1


            if i >= len_p:
                if window[s[i - len_p]] == 1:
                    del window[s[i - len_p]]

                else:
                    window[s[i - len_p]] -= 1

            if window == counter_p:
                result.append(i - len_p+1)           

        return result

s = Solution()
print(s.findAnagrams("cbaebabacd" ,"abc"))

        



