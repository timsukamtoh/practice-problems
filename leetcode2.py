"""
input: array of temps
return: array such that each element is the number of days until warmer temp or 0

ex: [30,60,90] => [1,1,0]

[70,60,90]

initial output
iterate through array current temp is at index i
    iterate through array at index i+k
        if temp at k > i,
            append k-i to output array
            break
    if len of output is not equal to given index + 1
        append 0 to output array
return output at end

"""


# def days_till_warmer(temps):
#     warmer_days = []

#     for i in range(len(temps)):
#         for k in range(i, len(temps)):
#             if temps[k] > temps [i]:
#                 warmer_days.append(k-i)
#                 break
#         if len(warmer_days) != i+1:
#             warmer_days.append(0)

#     return warmer_days


"""
you're given a log of timestamp and ip address pairs. if an ip address has been visited count number of times in the window, return the list of ips.

3,52.0.19.9
3,9.9.9.9
4,52.0.19.9

count = 2
window = 1
is_valid(String log, int count, int window)
[52.0.19.9]
"""


"""visited(int timestamp, String ip) -> true or false
window = 3
count = 3

1, 1.1.1.1  // true
1, 1.1.1.1 // true
1, 1.1.1.1 // false
5, 1.1.1.1 // true
"""

"""
linked list remove nth node
given the head of a linked list, remove the nth node from the end
1,2,3,4,5 if n=2, remove 4 => 1,2,3,5

Listnode {
    self.val = 0
    self.next = None
}

Traverse linked list to end to find length
determine how far nth node is from front with length - n
traverse linked list a second time and remove nth node

1, 4, 7 n=1

"""

def remove_n_from_end(head, n):
    total_len = 0 # 3
    curr=head

    while curr:
        total_len+=1
        curr=curr.next

    how_far = 0 # 0
    curr=head # 1
    if n==total_len:
        head = curr.next
    else:
        while how_far < total_len - n - 1: #0
            curr=curr.next
            how_far+=1
        curr.next = curr.next.next

    return head


"""
    input: binary tree with left and right
    output: int of the max diameter

                1
            2(3)    3       => 3
        4       5
                    7


define helper function to recursively calculate depth of left and right
    if leaf node
        return 0
    return the recursive left max depth + recursive right max depth

define solution
    given a node
    initiate variable to keep track of max width
    create a stack to track nodes to visit with initial root
    while values in stack
        traverse tree
        calculate max width using recursive max width for that node
        compare max width with node width
        add children to stack

    return the max width

                1(4)
            2(3)      3       => 6
        4      5
    4                5
4                        5
"""

# def max_width(node):
#     output_width = 0
#     to_visit = [node]
#     def max_depth_of_left_or_right(node):
#         if not node:
#             return 0
#         return 1 + max(max_depth_of_left_or_right(node.left), max_depth_of_left_or_right(node.right))


#     while to_visit:
#         curr = to_visit.pop()
#         node_depth = max_depth_of_left_or_right(node)

#         output_width = max(node_depth, output_width)
#         if curr.left:
#             to_visit.append(curr.left)
#         if curr.right:
#             to_visit.append(curr.right)

#     return output_width



"""
    input: an m x n matrix
    return: boolean if target value is in matrix

    all the rows are sorted in non-decreasing order
    first value of each row is greater than last value of prev row
    time complexity is o(log(nxm))

"""

"""

    use binary search twice
    first iteration is to find the row the value is in
    second iteration is to find the "supposed" position

    start_row will be top row
    end_row will be bottom
    while start_row less than end_row:
        mid_row is half of start plus end rows
        check if target is greater than first index of mid row and less than last index of midrow:
            target_row is equal to that index
            break out
        if target is less than first index of mid row
            move end row to mid row
        else
            move start row to row after mid row

    left is first index of target row
    right is last index of target row
    while left less than right:
        mid is half left and right
        check if target equal to mid:
            return true
        if target is less than mid
            move right to mid
        else
            move left to one after mid






"""


