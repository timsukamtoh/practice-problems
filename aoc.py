############ Advent of code puzzle questions ###############

"""
puzzle 1: calibration sum


"""

# def calibration_sum(input):
#     """
#     On each line, the calibration value can be found by
#     combining the first digit and the last digit (in that order)
#     to form a single two-digit number.

#     What is the sum of all the calibration values
#     """
#     def get_cal_value(code):
#         """
#         generate calibration value from a coded message
#         """
#         first = 0
#         second = 0

#         for i in range(len(code)):
#             if code[i].isdigit():
#                 second = int(code[i])
#             if code[len(code)-1-i].isdigit():
#                 first = int(code[len(code)-1-i])
#         return first*10 + second
#     lines = iter(input.splitlines())
#     total = 0
#     for line in lines:
#         total += get_cal_value(line)

#     return total

# print(calibration_sum(input))


"""
puzzle 2:
"""