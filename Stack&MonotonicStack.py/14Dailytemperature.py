class solution(object):
    def dailytemperature(self , temperature):
        stack = []
        res = [0]*len(temperature)

        for i , temp in enumerate(temperature):
            while stack and temp > stack[-1][0]:
                stackt , stackind = stack.pop()
                res[stackind] = (i - stackind)
            stack.append([temp , i])
        return res

s = solution()


# Call the function
print(s.dailytemperature([73, 74, 75, 71, 69, 72, 76, 73]))

