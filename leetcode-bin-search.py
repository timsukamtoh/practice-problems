#leetcode 704: Binary Search
def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1

###leetcode 74: Search a 2D Matrix###
def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    top, bot = 0, len(matrix) - 1
    while top <= bot:
        print(top, bot)
        mid = (top+bot)//2
        print(mid)
        if target >= matrix[mid][0] and target <= matrix[mid][len(matrix[mid])-1]:
            left, right = 0, len(matrix[mid])-1
            while left <= right:
                center = (left+right)//2
                if target == matrix[mid][center]:
                    return True
                elif target < matrix[mid][center]:
                    right = center - 1
                else:
                    left = center + 1
            return False
        elif target < matrix[mid][0]:
            bot = mid - 1
        else:
            top = mid + 1

    return False