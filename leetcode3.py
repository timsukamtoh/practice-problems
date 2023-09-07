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
def permute(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    permutations = []
    def choose_and_permute(perm, remaining)
        if not remaining:
            permutations.append(perm)
        else:
            while remaining:
                curr_val = remaining.pop()
