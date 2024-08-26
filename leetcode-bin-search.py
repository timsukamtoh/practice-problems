# leetcode 704: Binary Search
def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# leetcode 74: Search a 2D Matrix
def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    top, bot = 0, len(matrix) - 1
    while top <= bot:
        row = (top + bot) // 2
        if matrix[row][0] <= target <= matrix[row][-1]:
            left, right = 0, len(matrix[row]) - 1
            while left <= right:
                col = (left + right) // 2
                if target == matrix[row][col]:
                    return True
                elif target < matrix[row][col]:
                    right = col - 1
                else:
                    left = col + 1
            return False
        elif matrix[row][0] > target:
            bot = row - 1
        else:
            top = row + 1
    return False


# leetcode 875: Koko Eating Bananas
def minEatingSpeed(self, piles, h):
    """
    :type piles: List[int]
    :type h: int
    :rtype: int
    """
    biggest = max(piles)
    if h <= len(piles):
        return biggest

    def totalTimeToEat(rate: int) -> int:
        total_time = 0
        for pile in piles:
            if pile % rate == 0:
                total_time += pile // rate
            else:
                total_time += pile // rate + 1
        return total_time

    left = 1
    right = biggest
    slowest = biggest

    while left <= right:
        k = (left + right) // 2
        if totalTimeToEat(k) <= h:
            slowest = min(k, slowest)
            right = k - 1
        else:
            left = k + 1
    return slowest


# leetcode #153. Find Minimum in Rotated Sorted Array
def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    smallest = nums[0]
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        smallest = min(nums[mid], smallest)
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid - 1
    return smallest


# leetcode 33. Search in Rotated Sorted Array
def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > nums[right] and nums[right] >= target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
