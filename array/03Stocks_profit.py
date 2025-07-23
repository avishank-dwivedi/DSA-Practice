class solution(object):
    def findmediansortarray(self, prices):
        min_so_far = prices[0]
        max_profit = 0
        for price in prices:
            min_so_far = min(min_so_far , price)
            profit = price - min_so_far
            max_profit = max(max_profit, profit)
        return max_profit

si = solution()
print(si.findmediansortarray([5,4,2,9,5]))
