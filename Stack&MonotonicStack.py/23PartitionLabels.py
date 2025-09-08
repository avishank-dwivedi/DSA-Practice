class solution(object):
    def partition_label(self , s):
        last = {}
        for i , ch in enumerate(s):
            last[ch] = i

        res = []
        start , end = 0 , 0
        for i , ch in enumerate(s):
            end = max(end  , last[ch])

            if i == end :
                res.append(end - start + 1)
                start = i+1
        return res


s = solution()
print(s.partition_label("ababcbacadefegdehijhklij"))