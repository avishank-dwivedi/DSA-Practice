class solution(object):
    def valid_palindrom(self, str):
        start = 0
        end = len(str) -1

        while start < end:
            while start <end and not str[start].isalnum():
                start+=1
            while start <end and not str[end].isalnum():
                end-=1

            if str[start].lower()!= str[end].lower():
                return False
            start +=1
            end -=1
        return True


s = solution()
print(s.valid_palindrom("avishank assa KNAHSIVA"))



