""" input: array of integers
    output: array of integers in which every index is the product of the rest of the elems in the array excluding current index
    runtime: O(n)
    no division operator

    [1,3,2,4] => [24, 8, 12, 6]
    [1,1,1,1] => [1,1,1,1]


    initialize a return product at 1
    initialize a return array


    for integer inside elem


        multiply by the elem

"""

""" input: array of integers
    output: boolean that checks if there exists a triple of indices, such that the indices are in increasing sequence as well as their element

    [1,2,3] => true
    [3,2,1] => false
    [0,0,0] => false
    [1, 5, 7] => true
    [3, 1, 7] => false
    [1, 0, 2, 1, 6, 8] => true
    [1,3,0,5]
    [] => false

    instantiate tracker array
    traverse array
        keep track of current value
        if there is element with higher value:
            traverse through rest of array
                keep track of current value
                if there is element with higher value:
                    return True

    return False

"""
# [1, 0, 2, 1, 6, 8]
# def increasing_triple(nums):
#     for first_elem in nums: #[1, 0, 2, 1, 6, 8] @ 1
#         for second_elem in nums[nums.indexof(first_elem)+1:len(nums)]: #[0, 2, 1, 6, 8] @ 2
#             if second_elem > first_elem:
#                 for third_elem in nums[nums.indexof(second_elem)+1:len(nums)]: #[1,6,8] @ 6
#                     if third_elem > second_elem:
#                         return True

#     return False




""" input: array of integers
    output: will be an integer that is the pivot index in which everything to the left is equal to everything to the right

    [0, 0, 0, 0] => 0
    [1, 4, 6, 7, 1] => -1
    [1, 2, 5, 4, 4] => -1
    [1, 3, 5, 2, 2] => 2
    [1, 3, 1, 3] => -1

    instantiate index = 0

    instantiate left sum = first value
    instantiate right sum = last value

    iterate through list starting at i = 1
        if left sum == right sum and index == len(list)-index - 1
            return index
    return -1
    
"""

























