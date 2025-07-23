class Solution(object):
    def containsDuplicate(self, nums):
        
        seen = set()  # To store unique elements
        for num in nums:
            if num in seen:
                return True  # Duplicate found
            seen.add(num)
        return False  # No duplicates
    
s = Solution()
print(s.containsDuplicate([2, 3, 5, 6, 2])) 