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
"""
leetcode 2226: Maximum Candies to K Children
"""
# def maximumCandies(self, candies, k):
#     """
#     :type candies: List[int]
#     :type k: int
#     :rtype: int

#     >>> maximumCandies([4, 7, 5], 4)
#     3

#     """
#     most = 1
#     total = sum(candies)

#     if total < k:
#         return 0
#     left = 1
#     right = max(candies)
#     while left <= right:
#         pile_size = (left+right)//2
#         piles = 0
#         for p in candies:
#             piles += p//pile_size
#         if piles < k or pile_size*k > total:
#             right = pile_size-1
#         else:
#             most = max(most, pile_size)
#             left = pile_size+1

#     return most

"""
leetcode 138: copy list with random pointer
"""
# def copyRandomList(self, head):
#     """
#     :type head: Node
#     :rtype: Node
#     """
#     if not head:
#         return
#     pointers = {}
#     curr = head
#     while curr:
#         new_node = Node(curr.val)
#         pointers[curr] = new_node
#         curr = curr.next

#     curr = head
#     while curr:
#         copy = pointers[curr] if curr else None
#         copy.next = pointers[curr.next] if curr.next else None
#         copy.random = pointers[curr.random] if curr.random else None
#         curr = curr.next

#     return pointers[head]

"""
leetcode 2: add two numbers
"""
# def addTwoNumbers(self, l1, l2):
#     """
#     :type l1: ListNode
#     :type l2: ListNode
#     :rtype: ListNode
#     """

#     curr1 = l1
#     curr2 = l2
#     total = 0
#     length = 0
#     while curr1 or curr2:
#         total += curr1.val * 10**length if curr1 else 0
#         total += curr2.val * 10**length if curr2 else 0
#         curr1 = curr1.next if curr1 else None
#         curr2 = curr2.next if curr2 else None
#         length+=1

#     head = ListNode(0)
#     curr = head
#     if total == 0:
#         return head

#     while total > 0:
#         val = total%10
#         curr.next = ListNode(val)
#         total //= 10
#         curr = curr.next

#     return head.next

"""leetcode 287: Duplicate number"""
# def findDuplicate(self, nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     slow, fast = 0,0
#     while slow != fast or slow == 0:
#         slow = nums[slow]
#         fast = nums[nums[fast]]

#     start = 0
#     while start != slow:
#         start = nums[start]
#         slow = nums[slow]

#     return start

"""leetcode 739: daily temperatures"""
# def dailyTemperatures(self, temperatures):
#     """
#     :type temperatures: List[int]
#     :rtype: List[int]
#     """
#     stack = [] #[(6,76),(7,73)]
#     answer = [0]*len(temperatures) #[1,1,4,2,1,1,0,0]
#     for i in range(len(answer)):
#         while stack and temperatures[i] > stack[-1][1]:
#             stackI, stackT = stack.pop()
#             answer[stackI] = i - stackI
#         stack.append((i, temperatures[i]))
#     return answer