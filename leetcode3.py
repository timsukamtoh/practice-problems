""" A good node is a node in which on the path from it to the root node, it is the greatest
    can assume there will always be at least one good node


    ex [3,1,4,2] => 2 good nodes including root to root
                3
            /       \
        1               4
            \
                5


    initiate a current path which is a set of nodes that have been traversed to get to current node
    initiate a good nodes counter
    traverse the tree via dfs
        at each new node, check if current node val is greater than all node vals in current path
            if so, increment good nodes counter
        if we need to change branches
            delete branch nodes that are not part of current path

    return good nodes counter

    ex [3,1,4,5] => 3 total include root to root



"""

# def count_good_nodes(root):
#     total_good = 0
#     if not root:
#         return total_good
#     current_path = [root]

#     def dfs(node, current_path, total_good=total_good):
#         if not node:
#             return
#         if is_good_node(node, current_path=current_path):
#             total_good += 1
#         if node.left:
#             left_path = current_path.append(node.left)
#             dfs(node.left, left_path, total_good)
#         if node.right:
#             right_path = current_path.append(node.right)
#             dfs(node.right, right_path, total_good)

#     dfs(root, current_path)
#     return total_good



# current_path = [root.val]
# to_visit_stack = [root]

# while to_visit_stack:
#     curr = to_visit_stack.pop()
#     if is_good_node(curr, current_path):
#         total_good += 1
#     if curr.right:
#         to_visit_stack.append(curr.right)
#     if curr.left:
#         to_visit_stack.append(curr.left)


# def is_good_node(node, current_path):
#     for node_val in current_path:
#         if node.val < node_val:
#             return False
#     return True


"""
    leetcode 160: intersection of two linked lists
"""
# def getIntersectionNode(self, headA, headB):
#     stackA = ['A']
#     stackB = ['B']

#     while headA or headB:
#         if headA:
#             stackA.append(headA)
#             headA = headA.next

#         if headB:
#             stackB.append(headB)
#             headB = headB.next

#     prev = None
#     while stackA and stackB:
#         nodeA = stackA.pop(-1)
#         nodeB = stackB.pop(-1)

#         if nodeA != nodeB:
#             return prev

#         prev = nodeA

"""
    leetcode 15: threesum
"""
# def threeSum(self, nums):
#     target = 0
#     nums.sort()
#     triples = set()
#     for i, a in enumerate(nums):
#         if a > 0:
#             break
#         if i > 0 and a == nums[i-1]:
#             continue
#         j = i + 1
#         k = len(nums)-1
#         while j < k:
#             total = nums[i] + nums[j] + nums[k]
#             if total == target:
#                 triples.add((nums[i], nums[j], nums[k]))
#                 j += 1
#                 k -= 1
#             elif total < target:
#                 j += 1
#             else:
#                 k -= 1

#     return list(triples)

"""
    input: given a root of a node
    output: boolean if entire tree is a valid BST

    ex:
    [5, 1, 6, null ,null, 3, 7] => invalid
    [5, 2, 8, null ,3, 6, 9, 1] => invalid
    [2,1,3] => valid

    initiate a seen values
    define recurisve function
        if we get to a leaf node
            return true
        if left is greater than root
            return false
        if right is smaller than root
            return false
        otherwise
            make a copy of our seen values + left
            update our seen values + right
            check if every value in right is greater than root AND every value left of root is smaller

    return execute recursive call


"""
# def validate_bst(root):
#     if not root:
#         return True

#     def validate_values(node, lower, upper): #2
#         if not node.left and not node.right:

#             return True
#         if (node.left and node.left.val > node.val) or (node.left.val > lower):
#             return False
#         if (node.right and node.right.val < node.val) or (node.right.val < upper): #3
#             return False
#         return validate_values(node.left, lower, node.val) and validate_values(node.right, node.val, upper)

#     return validate_values(root, -infinity, Infinity)

"""
    leetcode 46: Permutations
"""
# def permute(self, nums):
#     """
#     :type nums: List[int]
#     :rtype: List[List[int]]
#     """
#     permutations = []
#     def backtrack(curr):
#         if len(curr) == len(nums):
#             permutations.append(curr[:])
#             return

#         for num in nums:
#             if num not in curr:
#                 curr.append(num)
#                 backtrack(curr)
#                 curr.pop()

#     backtrack([])
#     return permutations


"""
    input: given a root, and int k
    output: return kth smallest value

    ex ipnut: ([3, 1, 4, null, 2], 1) =>  1
    positve, unique, and at least 1 node


            3
          /   \
        1       4
          \
            2

    initiate list for all tree values
    recursively, traverse through tree
        store tree values in list of tree values

    sort list
    return k-1 from start of list


"""

# def kthSmallest(self, root, k):
#     """
#     :type root: TreeNode
#     :type k: int
#     :rtype: int
#     """
#     node_vals = []
#     def traverse(node):
#         if not node:
#             return
#         else:
#             node_vals.append(node.val)
#             traverse(node.left)
#             traverse(node.right)

#     traverse(root)
#     node_vals.sort()
#     return node_vals[k-1]

"""
    leetcode 105: Construct binary tree from preorder and inorder transversal
"""
# def buildTree(self, preorder, inorder):
#     """
#     :type preorder: List[int]
#     :type inorder: List[int]
#     :rtype: TreeNode
#     """

#     if len(preorder) <= 0:
#         return None

#     current_node = TreeNode(preorder[0])

#     index_of_curr = inorder.index(current_node.val)
#     left_in_order = inorder[:index_of_curr]
#     right_in_order = inorder[index_of_curr+1:]

#     left_pre_order = preorder[1:1+len(left_in_order)]
#     right_pre_order = preorder[1+len(left_in_order):]

#     current_node.left = self.buildTree(left_pre_order, left_in_order)
#     current_node.right = self.buildTree(right_pre_order, right_in_order)

#     return current_node

"""
    leetcode 103: Binary Tree Zigzag Level Order Traversal
"""
# def zigzagLevelOrder(self, root):
#     """
#     :type root: TreeNode
#     :rtype: List[List[int]]
#     """
#     if not root:
#         return []

#     queue = [root]
#     ltr = True
#     result = []

#     while queue:
#         level = []
#         size = len(queue)
#         for i in range(size):
#             curr = queue.pop(0)
#             level.append(curr.val)
#             if curr.left:
#                 queue.append(curr.left)
#             if curr.right:
#                 queue.append(curr.right)

#         if ltr:
#             ltr = False
#         else:
#             level = level[::-1]
#             ltr = True
#         result.append(level)

#     return result




"""
    input: string containing digits from 2-9 inclusive
    output: list of strings that have all combinations

    ex "23" => [ "AD", "AE", "AF", "BD" ... ]

    define string_permutations (string):
        initiate digit to letter hashmap
        n = len(string)

        list of group of chars = {}
        for every char in our input
            append the value from key-value of string in hashmap to the list of groups

        group of chars  = {"2":"abc", "3":"def",...,[w,x,y,z]}

        output = []

        def backtracking(current permutation = "", index=0):
            if len(current_permutation) is equal n
                output append current_permutation
                return
            for i in range (group of chars[string[index]]):
                current_permutation add char at group[i]
                call backtracking on the next group_of_chars(current permutation + i, index +1)

        call backtracking on group of chars
        return output

"""
"""
    leetcode 79: word search

    def check_word(string, row, col, seen):
            if len(string) == 0:
                return True
            if (row, col) in seen:
                return False
            if row < 0:
                return False
            if col < 0:
                return False
            if row >= len(board):
                return False
            if col >= len(board[row]):
                return False
            if string[0] != board[row][col]:
                return False
            print("row ",row , "col ", col)
            seen.add((row,col))
            return check_word(string[1:], row - 1, col, set(seen)) or check_word(string[1:], row, col - 1, set(seen)) or check_word(string[1:], row + 1, col, set(seen)) or check_word(string[1:], row, col + 1, set(seen))


        for i in range(len(board)):
            for j in range(len(board[i])):
                seen = set()
                if check_word(word, i, j, seen):
                    return True
        return False
"""
"""
    leetcode 22: Generate Parenthesis
"""
# def generateParenthesis(self, n):
#     """
#     :type n: int
#     :rtype: List[str]
#     """
#     perms = []
#     options = ["(",")"]
#     def add_parens(left, right, current_parens):
#         if len(current_parens) == 2*n:
#             perms.append(current_parens)
#             return
#         if left < n:
#             str1 = current_parens + "("
#             add_parens(left + 1, right, str1)
#         if right < left:
#             str2 = current_parens + ")"
#             add_parens(left, right+1, str2)
#     add_parens(0,0,"")
#     return perms

"""
    input: given a string
    output: return a list of list of strings where every string elem is a palindrome
    "baab" => [[b,a,a,b],[b,aa,b], [baab]]
    "bbaab" => [[b,b,a,a,b], [bb, a, a,b], [bb,aa,b],[b,b,aa,b], [b,baab]]

    initiate list of palindromes
    recursive function (index, current palindrome list)
        if index >= len(string)
            we can add the current palindrome list to list of palindromes
            return
        if string is palindrome then we
            add to list of current list of palidromes
        recursive function call on (string[index +1], current palindrome list)
        recursive function call on (string[index] + string[index + 1], current palindrome list)



    is palindrome function(string)
        for i in range(len(string)):
            if string at index i not equal to opposite end at string
                return false
        return true

    "baab" => [[b,a,a,b],[b,aa,b], [baab]]
    "bbaab" => [[b,b,a,a,b], [bb, a, a,b], [bb,aa,b],[b,b,aa,b], [b,baab]]
"""
# def generate_palindromes(string):

#     def is_palindrome(string):
#         for i in range(len(string)//2 + 1):
#             if str1[i] != str1[len(str1)-1-i]:
#                 return False

#         return True

#     list_of_palindromes = [] #[[b,a,a,b], ]
#     current_palindrome = []
#     #left =1  right=1
#     def recurive_build_palindrome(index): #[b, a, aa,]
#         if index > len(string):
#             list_of_palindromes.append(current_palindrome)
#             return
#         for j in range(len(string)):
#             if is_palindrome(string[index:j+1]):
#                 current_palindrome.append(string[index:j+1])
#                 recurive_build_palindrome(j+1)
#                 current_palindrome.pop()
#     recurive_build_palindrome(0)
#     return list_of_palindromes

"""
    leetcode 56: merge intervals
"""
# def merge(self, intervals):
#     """
#     :type intervals: List[List[int]]
#     :rtype: List[List[int]]
#     """
#     intervals.sort(key=lambda x:x[0])

#     def check_next(index):
#         if index >= len(intervals):
#             return
#         output_end = output[len(output)-1]
#         if intervals[index][0] <= output_end[1]:
#             start, end = output_end[0], intervals[index][1]
#             if intervals[index][0] < output_end[0]:
#                 start = intervals[index][0]
#             if intervals[index][1] < output_end[1]:
#                 end = output_end[1]
#             output[len(output)-1] = [start, end]
#         else:
#             output.append(intervals[index])
#         return check_next(index+1)

#     output = [intervals[0]]
#     check_next(1)
#     return output


"""
    reverse polish notation examples:
    ["2", "1", "+", "3", "*"] => 9
    ["4", "13", "5", "/", "+"] => 6


    initiate stack
    initiate hashmap of string operator to actual operator
    iterate through given array of strings
        if string can be converted to int
            append int to stack
        otherwise
            we retrieve operation from hashmap
            pop off 2 values from the stack which will be our operands
            append result of operation to stack

    return last value of array
"""

# def reverse_polish_math(values):
#     int_stack = []
#     operations = {"+":lambda (x,y): x+y, "*",lambda (x,y): x*y,"/":lambda (x,y): x/y, "-":lambda (x,y): x-y}

#     for val in values:
#         if val in operations:
#             second = int_stack.pop()
#             first = int_stack.pop()
#             result = operations[val](first, second)
#             int_stack.append(result)
#         else:
#             int_stack.append(int(val))

#     return int_stack.pop()

"""leetcode 198: House Robber"""
# def rob(self, nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """

#     # if len(nums) == 0:
#     #     return 0
#     # if len(nums) <= 2:
#     #     return max(nums)
#     # else:
#     #     return max(nums[0] + self.rob(nums[2:]), nums[1] + self.rob(nums[3:]))

#     #[9,1,1,9,1]


#     robbed = [nums[0]] #[9, 1, 10, 18
#     max_value = nums[0] # 10

#     for i in range(1, len(nums)):
#         if len(robbed) < 2:
#             robbed.append(nums[i])
#         else:
#             max_money = robbed[i-2] + nums[i] #18
#             if len(robbed) >= 3:
#                 max_money = max(max_money, nums[i] + robbed[i-3])
#             robbed.append(max_money)
#         max_value = max(robbed[i], robbed[i-1])

#     return max_value

"""
    multiply strings

    input: 2 non negative strings that are ints
    return: the multiplication of 2 ints


    cant use built in convert methods (on the inputs)

    def multiply strings method
        def convert string helper method takes in str
            initiate number = 0
            for char in str
                number plus the conversion of the char to int multiplied by 10 raised to power index i
            return number

        execute helper on both strings
        multiply both results together
        return string version

    "100" "20" => 2000
    "0" "12321" => 0

"""

# def multiply_strings(str_int1, str_int2):
#     def convert_string(string_int): #100
#         number = 0
#         size = len(string_int)
#         for i in range(size):
#             number += int(string_int[size-i-1]) * 10**i
#         return number
#     int1, int2 = convert_string(str_int1), convert_string(str_int2)
#     return f"{int1 * int2}"


"""
    leetcode 647: palindromic Substrings
"""
# def countSubstrings(self, s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     start_to_end = [[False]*len(s) for letter in s]
#     num_palindromes = len(s)

#     for i in range(len(start_to_end)):
#         start_to_end[i][i] = True
#     for j in range(len(s)):
#         for i in range(j):

#             if s[i] == s[j] and (start_to_end[i+1][j-1] or j-i == 1):
#                 num_palindromes += 1
#                 start_to_end[i][j] = True
#     print(start_to_end)

#     return num_palindromes

"""
    input: given an array of ints
    out: return nums of valid paris where a valid pair is a pair of ints that are only differing by at most 1 digit

    [240, 241, 243, 1, 9] => 4

    all non-negative

    def solution
        initiate counter for num pairs
        convert array of ints into array of strs
        iterate through the array of strs
            double for loop compare current value to remaining values
                initiate a digits off integer tracker to 0
                check lens if not equal
                    continue
                iterate through str
                    if a char within the str is not equal
                        increment digits off
                check if digits off is less than or equal 1
                    increment num pairs
        return num pairs

"""

# def valid_pairs(ints):
#     num_pairs = 0 #4
#     string_ints = ints.map(key=lambda x: f"{x}")

#     for i, string in enumerate(string_ints):
#         for j in range(i+1, len(string_ints )):
#             digits_off = 0
#             string2 = string_ints[j] #240, 241
#             if len(string) != len(string2) or string == string2:
#                 continue
#             for k in range(len(string)):
#                 if string[k] != string2[k]:
#                     digits_off += 1
#             if digits_off <= 1:
#                 num_pairs += 1

#     return num_pairs


"""
    leetcode: coinchange2
"""
def change(self, amount, coins):
    # """
    # :type amount: int
    # :type coins: List[int]
    # :rtype: int
    # """
    # total_ways = 0 #2
    # stored = {}

    # def count_ways(value, index):
    #     if value < 0:
    #         return 0
    #     if value == 0:
    #         return 1
    #     temp = 0
    #     for i in range(index, len(coins)):
    #         if (value, i) in stored:
    #             return stored[(value, i)]
    #         temp += count_ways(value - coins[i], i)
    #     stored[(value, index)] = temp
    #     return temp
    #     #countways(4,0)
    #         #countways(3,0)
    #             #countways(2,0)
    #                 #countways(1,0)
    #                     #countways(0,0)
    #                 #countways(0,1)
    #             #countways(1,1)
    #                 #countways(-1,1)
    #                 #countways(-4,2)
    #             #countways(-2,2)
    #         #countways(2,1)
    #             #countways(1,0)
    #             #countways(0,1)
    #             #countways(-3,2)
    #         #countways(-1,2)
    #     #countways(3,1)
    #     #countways(0,2)


    # return count_ways(amount, 0)

"""
    leetcode 55: jump game
"""
# def canJump(self, nums):
#     """
#     :type nums: List[int]
#     :rtype: bool
#     """

#     size = len(nums)
#     search_index = size-1

#     for i in range(size):
#         if nums[size-1-i] + (size-1-i) >= search_index:
#             search_index = size-1-i
#     if search_index == 0:
#         return True
#     return False

"""
    input: given a string s
    output: return the number palindromic subsequences

    "abba" => [a,b,b,a, bb, abba] = > 6

    helper function takes in a string
        iterate through string
            if forward i not equal to backward i
                return false
        return true

    recursive function that takes in left right index
        check if left or right is oob
            return
        check if whole string is palindrome
            store inside set
            increase count
            return recursively call on string + left and right index

    initiate a counter of palindromes
    create a palindrome set
    for every letter
        check if its in the palindome set
            if is, return true
        if not, we check if palindrome
            if is, add to set
                check recursively

    "abba" => [a,b,b,a, bb, abba] = > 6

"""
# def num_subsequence_palindromes(string):
#     num_palindromes = 0

#     def keep_check_palindrome(left, right):
#         if left < 0 or right > len(string) - 1:
#             return
#         if string[left] != string[right]:
#             return
#         num_palindromes += 1
#         return keep_check_palindrome(left-1, right+1)

#     for i in range(len(string)):
#         if is_palindrome(string[i]):
#             num_palindromes += 1
#             keep_check_palindrome(i-1, i+1)
#             keep_check_palindrome(i, i+1)

#     return num_palindromes

# def is_palindrome(string):
#     for i in range(len(string)):
#         if string[i] != string[len(string-i-1)]:
#             return False
#     return True

"""
    leetcode 48: rotate an image

"""
# def rotate(self, matrix):
#     """
#     :type matrix: List[List[int]]
#     :rtype: None Do not return anything, modify matrix in-place instead.

#     >>>a = [[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]]
#     >>>solution(a)
#     [[7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3]]

#     """

#     for r in range(len(matrix)):
#         for c in range(r , len(matrix[0])):
#             temp = matrix[r][c]
#             matrix[r][c] = matrix[c][r]
#             matrix[c][r] = temp
#         matrix[r].reverse()



"""
    mximum product subarray:

    input: nums
    return: largest product of conintuous subarray

    initiate a max product = 1
    curr product = 1
    create a structure to store absolute max
    local min and local max
    keep track of number of negatives

    iterate through nums:
        curr_product  will become curr_product * num
        compare local max to curr_product and set to local max
        compare local min to curr_product and set to local min
        compare absolute to local max and set to absolute
        if number negatives is divisbile by 2
            compare absolute to local min

    return absolute max


    [2,1,0,1,1,6]
"""
# def maxProduct(self, nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     absolute_product = nums[0]
#     local_max = 1
#     local_min = 1

#     for num in nums:
#         temp = num * local_max
#         local_max = max(temp, num* local_min, num)
#         local_min = min(temp, num* local_min, num)
#         absolute_product = max(local_max, absolute_product)

#     return absolute_product

"""
leetcode 53: max subarray sum
"""
# def maxSubArray(self, nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     left, right = 0,0
#     max_sum = nums[0]
#     curr_sum = 0
#     while right < len(nums):
#         curr_sum += nums[right]
#         max_sum = max(max_sum, curr_sum)
#         if curr_sum < 0:
#             left = right
#             curr_sum = 0
#         right += 1

#     return max_sum

"""
min flips
input: target string of same length
    start from a string of 5 zeros
output: return num of flips

ex:
target: 01011 given: 01011
                      ^^^
return 3


initiate num of flips
initiate final str
initiate str of current "value"

iterate through target string from front to back
    if the current char in target string is equal to current "value"
        continue
    else:
        flip current value
        and increment num flips

"""

# def min_flips(target): #01011
#     num_flips = 0 #3
#     current = "0" #1
#     for char in target: #1
#         if char == current:
#             continue
#         else:
#             num_flips += 1
#             current = char
#     return num_flips

"""
input: num rows
output: num rows of rows in pascals triangle

                1
            1        1
        1       2       1
    1       3       3       1
1       4       6       4       1

output = [[1]]
if num rows is 1
    return output

last row will be initialized to [1, 1]

if num rows is 2
    return ouput appended with last row


iterate through the num of rows in a range from 2 to num rows
    curr row set to empty array
    iterate through curr row and build on it + 1 in range since we want to keep increasing length of row
        if  index is 0 or index is equal to length of last row
            current append 1
        else
            current row append last row at index + last row at index - 1
    output append curr row
    last_row = output last elem

return output
"""

# def pascals_rows(num_rows): #5
#     output = []
#     if num_rows == 0:
#         return output
#     for r in range(num_rows):
#         last_row = output[-1]
#         curr_row = []
#         for i in range(len(last_row)+1):
#             if i == 0 or i == len(last_row):
#                 curr_row.append(1)
#             else:
#                 curr_row.append(last_row[i] + last_row[i-1])
#         output.append(curr_row)


#     return output
