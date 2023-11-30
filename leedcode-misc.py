"""
    leetcode 1929: Concatenation
"""
# def getConcatenation(self, nums):
#     """
#     :type nums: List[int]
#     :rtype: List[int]
#     """
#     ans = [0]*2*len(nums)
#     for i in range(0, len(nums)):
#         ans[i] = nums[i]
#     for i in range(len(nums), len(ans)):
#         ans[i] = nums[i-len(nums)]
#     return ans