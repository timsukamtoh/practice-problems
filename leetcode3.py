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
def getIntersectionNode(self, headA, headB):
    stackA = ['A']
    stackB = ['B']

    while headA or headB:
        if headA:
            stackA.append(headA)
            headA = headA.next

        if headB:
            stackB.append(headB)
            headB = headB.next

    prev = None
    while stackA and stackB:
        nodeA = stackA.pop(-1)
        nodeB = stackB.pop(-1)

        if nodeA != nodeB:
            return prev

        prev = nodeA