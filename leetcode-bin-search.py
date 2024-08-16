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


# leetcode 74: Search a 2D Matrix###
def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    top, bot = 0, len(matrix)-1
    while top <= bot:
        row = (top + bot)//2
        if matrix[row][0] <= target <= matrix[row][-1]:
            left, right = 0, len(matrix[row])-1
            while left <= right:
                col = (left + right)//2
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