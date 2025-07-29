from collections import defaultdict
class solution(object):
    def groupAnabram(self , strings:str ):

        stor = defaultdict(list)
        

        for str in strings:
            stored_word = ''.join(sorted(str))
            stor[stored_word].append(str)


            
        return list(stor.values())

so = solution()
print(so.groupAnabram(["eat", "tea", "tan", "ate", "nat", "bat"]))