class solution(object):
    def ValidAnagram(self , s: str , t: str) -> bool:

        if len(s) != len(t):
            return False
    
        countS = {}
        countT = {}

        for ch in s:
           countS[ch] = countS.get(ch , 0)+ 1

        for ch in t:
            countT[ch]  = countT.get(ch ,0)+ 1

        return countS == countT

ss = solution()
print(ss.ValidAnagram("string","ginstr"))