"""
leetcode 2789: largest element after merge operations
"""
# def maxArrayValue(self, nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     dp = nums[:]

#     for i in range(len(nums)-1, 0, -1):
#         if len(nums) == 0:
#             return nums[0]
#         if nums[i-1] > nums[i]:
#             continue

#         nums[i-1] += nums[i]
#         dp[i-1] += dp[i]
#         nums.pop(i)

#     return max(dp)