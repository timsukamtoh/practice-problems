# """ Hello world => dlrow olleH"""

# """ initialize empty string
#     for every char in string go from end to front
#         add that char to the empty string
#     return string"""

# def reverse_string(string):
#     answer = ""
#     for i in range(len(string)):
#         answer += string[len(string)-i-1]
#     return answer


# """ input: is a string
#     output will be a boolean that is true if more than 50% are vowels
# """

# """ initialize list of vowels
#     initialize count of vowels
#     iterate through array
#         if char is a in vowel array, then add to count
#     return if the count is > len(string)/2
# """
# def mostly_vowels(string):
#     vowels = ['a','e','i','o','u']
#     vowel_count = 0
#     for char in string:
#         if char in vowels:
#             vowel_count += 1
#     return vowel_count >= len(string)/2

# """ input: list of numbers
#     true if any 2 numbers add to 0"""

# """ initialize an object of seen values
#     iterate through array
#         if the number we need to add to the current indexed value in the seen object, can return true
#     return false
# """

# """[3, 4, 2, 7, -5, -3] => true"""

# def sum_to_zero(nums):
#     seen = {}
#     for num in nums:
#         if (-num) in seen:
#             return True
#         seen.add(num)
#     return False




""" input: list of numbers
    output: the greatest value within the list
"""

""" [-8, 5, 3, 9, 0] => 0"""

""" initialize return number to be 0
    iterate through the list
        compare the current index value to the greatest
            set greatest to current if current is bigger
    return greatest
"""
# greatest = 9
# current = 0

def find_greatest(nums=[]):
    greatest = 0
    for num in nums:
        if num > greatest:
            greatest = num
    return greatest


""" input: string
    output: boolean if is palindrome
"""
