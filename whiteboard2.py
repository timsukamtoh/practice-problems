# """ input: array
#     function: duplicate zeros and keep array length the same
#     output: none

#     test case: [1, 0, 2, 0, 3]
#     result: [1, 0, 0, 2, 0]
# """
def dup_zeros(nums):
    original_length = len(nums)
    print(original_length)

    i=0
    while i < original_length:
        if(nums[i] == 0):
            i+=1
            nums.insert(i, 0)
            print(i)
        i+=1

    nums[:] = nums[:original_length]
    print(nums)



""" input: array of strings that represents a poker hand
    output: boolean if hand contains an straight

    test: ["3S", "5D", "2C", "6S", "4H"] => true
        [1, 5, 6, 8, 9]=> false
        [2H, 2D, 2C, 2S, 3C]
        [AS, KS, QS, JS, 10S]

    loop through list
    create a separate list of just values of the cards in the hand
    start at the min value and loop to 5
        check if each increment exists within separate list of just values
        return false if it doesn't
    return true

"""
# hand: [AS, KS, QS, JS, 10S]

# values: [A, K, Q, J, 10]
def has_straight(hand):
    deck = [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    values = []

    for card in hand:
        if(card[1] == "0"):
            values.append(card[0:2])
        else:
            values.append(card[0])

    starting = 12

    for card_val in values:
        if deck.index(card_val) < starting:
            starting = deck.index(card_val) #starting: 9

    for i in range(starting, starting+5): #9-14
        if deck[i] not in values:
            return False

    return True



""" input: 1st array of positive ints, int
    output: array of boolean on if the value after 2nd int is added to each index is greater than max

    test case: ([3,7,2,8], 5) => [false, true, false, true]

    find and store the max of the arr
    initialize a new array for boolean values
    iterate through the first array and apply the following:
        initialize current value which is the sum of the value at index and the int input
        compare that with the max of the array
        boolean arr push(current > max_candies)

    return boolean array

"""

# ([3,7,2,8], 5)
def more_candies_than_max(candies, increase):
    max_candies = max(candies) #8
    boolean_arr = []

    for candy in candies: #8
        current = candy + increase #13
        boolean_arr.append(current>max_candies)

# [False, True, False, True]
    return boolean_arr

