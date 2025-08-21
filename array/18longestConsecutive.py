class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums = sorted(set(nums))  # remove duplicates & sort
        longest = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:  # consecutive
                count += 1
                longest = max(longest, count)
            else:
                count = 1  # reset

        return longest
    

nums = [100, 4, 200, 1, 3, 2]
print(Solution().longestConsecutive(nums))  # Output: 4 (sequence 1,2,3,4)
