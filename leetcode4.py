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

"""
leetcode 875: Koko Eating Bananas
"""
# def minEatingSpeed(self, piles, h):
#     biggest = max(piles)
#     if h <= len(piles):
#         return biggest

#     def hours_to_eat(rate):
#         total_h = 0
#         for pile in piles:
#             if pile % rate == 0:
#                 total_h += pile//rate
#             else:
#                 total_h += pile//rate + 1
#         return total_h

#     left = 1
#     right = biggest
#     slowest = biggest
#     while left <= right:

#         k = (left + right)//2
#         print(k)

#         if hours_to_eat(k) <= h:
#             slowest = min(k, slowest)
#             right = k-1
#         else:
#             left = k + 1
#     return slowest