class Game:
    # initialization function
    def __init__(self, coins):
        # initialize coin array
        self.coins = coins
        # variable n for length of coin array + 1, this will be the size of column and rows of our 2-D array.
        n = len(coins) + 1

        # Using list comprehension to create n x n 2-D array with each element initialized to (-1, -1, -1). This will be
        # used as the data structure to hold previously calculated sub-problems and avoid having to recalculate them.
        self.dataStruct = [[(-1, -1, -1) for row in range(n)] for column in range(n)]


    def run(self, start, end):
        # index variables
        maxWinIndex = 0
        marginIndex = 1
        takeRightIndex = 2


        max_win = 0
        margin = 0
        takeRight = True
        # Do the calculation

        # base case when there are no coins left, and this occurs when the start index > end index or vice versa
        if((start > end) or (end < start) or (len(self.coins) == 0)):
            # max_win will be 0, margin will be 0, and takeRight = true by default
            return (max_win, margin, takeRight)

        # base case when there is only one coin left start index = end index
        elif (start == end):
            # max_win will be the value of this last coin
            max_win += self.coins[start]
            # margin will be the value of this lat coin
            margin += self.coins[start]
            # return max_win, margin, and takeRight = true by default
            return (max_win, margin, takeRight)


        # check data structure, if at this start and end index it isn't -1 then it has a previous calculated value
        # so we will utilize this value
        if(self.dataStruct[start][end] != (-1, -1, -1)):
            return self.dataStruct[start][end]


        # recursive calls

        # variables to hold the result of recursing left and right
        left = 0
        right = 0


        # if current player picked the left coin

        # get value of left coin at start index
        leftCoinValue = self.coins[start]

        # opponent also picks left, so this is the value we get if we recurse on the array after their pick
        # start index + 2 because both current player and opponent picks left so we must remove 2 coins from the left
        # end index doesn't change
        LOppLeft = self.run((start + 2), end)

        # opponent picks right, so this is the value we get if we recurse on the array after their pick
        # start index + 1 because we picked left and so we must remove a coin from the left, end index is end - 1
        # because the opponent takes a coin from the right
        LOppRight = self.run((start + 1), (end - 1))


        #variable for left margin
        Lmargin = 0


        # pick the array that yields the smallest total coin value after the opponent makes their pick, because the
        # the opponent is also trying to win!
        if(LOppLeft[maxWinIndex] < LOppRight[maxWinIndex]):
            # left margin is the recursive margin from current player pick left and the opponent picking left +
            # left coin value - the opponent's left coin value
            Lmargin = LOppLeft[marginIndex] + leftCoinValue - self.coins[start + 1]
            # value of recursing left is now based on the min array LOppLeft
            left = LOppLeft[maxWinIndex] + leftCoinValue

        # if LOppLeft >= LOppRight we will take LOppRight, especially when both are equal because we take right by default
        else:
            # left margin is the recursive margin from current player pick left and the opponent picking right + left
            # coin value - opponent's right coin
            Lmargin = LOppRight[marginIndex] + leftCoinValue - self.coins[end]
            # value of recursing left is now based on the min array LOppRight
            left = LOppRight[maxWinIndex] + leftCoinValue


        # if current player picked the right coin

        # get value of right coin at end index
        RightCoinValue = self.coins[end]

        # opponent picks left, so this is the value we get if we recurse on the array after their pick
        # start index + 1 because the opponent picks left, and end index is end - 1 because current player picked right
        ROppLeft = self.run((start + 1), (end - 1))

        # opponent picks right, start index is start because no one picked left, end index is end - 2 because both the
        # current player and the opponent picked right
        ROppRight = self.run(start, (end - 2))


        # variable for the right margin
        Rmargin = 0

        # pick the array that yields the smallest total coin value after the opponent makes their pick, because the
        # the opponent is also trying to win!
        if (ROppLeft[maxWinIndex] < ROppRight[maxWinIndex]):
            # right margin is the recursive margin from current player pick right and the opponent picking left + right
            # coin value - opponent's left coin
            Rmargin = ROppLeft[marginIndex] + RightCoinValue - self.coins[start]
            # value of recursing right is now based on the min array ROppLeft
            right = ROppLeft[maxWinIndex] + RightCoinValue

        # if ROppLeft >= ROppRight we will take ROppRight, especially when both are equal because we take right by default
        else:
            # right margin is the recursive margin from current player pick right and the opponent picking right + right
            # coin value - opponent's right coin
            Rmargin = ROppRight[marginIndex]+ RightCoinValue - self.coins[end - 1]
            # value of recursing right is now based on the min array ROppRight
            right = ROppRight[maxWinIndex] + RightCoinValue



        # if left max value > right, assign the max_win, margin, and take right to be based on the left recursion
        if(left > right):
            max_win = left
            margin = Lmargin
            takeRight = False
        # otherwise if right >= left, assign the max_win, margin, and take right to be based on the right recursion
        else:
            max_win = right
            margin = Rmargin
            takeRight = True

        # store recursive data into data structure
        self.dataStruct[start][end] = (max_win, margin, takeRight)

        # return values
        return (max_win, margin, takeRight)





# Tests, Remove before submission

print("Testing Prof's tests:")

coingame = Game([4, 4, 9, 4, 1, 2, 3])
print(coingame.run(0, 3)) # (13, 5, False)
print(coingame.run(0, 4)) # (12, 2, False)
print(coingame.run(2, 2)) # (9, 9, True)
print(coingame.run(4, 6)) # (4, 2, True)

print(coingame.run(1,3)) # (8, -1, True)
print(coingame.run(1,0)) # (0, 0, True)

try:
    assert coingame.run(0, 3) == (13, 5, False)
    assert coingame.run(0, 4) == (12, 2, False)
    assert coingame.run(2, 2) == (9, 9, True)
    assert coingame.run(4, 6) == (4, 2, True)
    assert coingame.run(1, 3) == (8, -1, True)
    assert coingame.run(1, 0) == (0, 0, True)
    print("All tests passed!")
except AssertionError:
    print("Test failed!")


print("\n")
print("Testing No coin game:")
coingame_empty = Game([])
try:
    assert coingame_empty.run(0, 0) == (0, 0, True)
    print("All tests passed!")
except AssertionError:
    print("Test failed!")


print("\n")
print("Testing 1 coin game:")
coingame_1 = Game([5])
try:
    assert coingame_1.run(0, 0) == (5, 5, True)
    print("All tests passed!")
except AssertionError:
    print("Test failed!")


print("\n")
print("Testing 2 coin game:")
coingame_2 = Game([5,6])
try:
    assert coingame_2.run(0, 1) == (6, 1, True)
    assert coingame_2.run(0, 0) == (5, 5, True)
    assert coingame_2.run(1, 1) == (6, 6, True)
    print("All tests passed!")
except AssertionError:
    print("Test failed!")


print("\n")
print("Testing 3 coin game:")
coingame_3 = Game([5,6,7])
try:
    assert coingame_3.run(0, 2) == (12, 6, True)
    assert coingame_3.run(1, 1) == (6, 6, True)
    assert coingame_3.run(2, 2) == (7, 7, True)
    assert coingame_3.run(0, 1) == (6, 1, True)
    assert coingame_3.run(1, 2) == (7, 1, True)

    print("All tests passed!")
except AssertionError:
    print("Test failed!")


print("\n")
print("Testing Large values coin game:")
coingame_large_values = Game([1000, 2000, 3000, 4000])
try:
    assert coingame_large_values.run(0, 3) == (6000, 2000, True)
    print("All tests passed!")
except AssertionError:
    print("Test failed!")



print("\n")
print("Testing start index > end index:")
coingame_invalid_index = Game([1000, 2000, 3000, 4000])
try:
    assert coingame_invalid_index.run(3, 1) == (0, 0, True)
    assert coingame_invalid_index.run(4, -1) == (0, 0, True)
    print("All tests passed!")
except AssertionError:
    print("Test failed!")


print("\n")
print("Testing left:")
coingame_left = Game([5000, 4000, 3000, 2000])
try:
    assert coingame_left.run(0, 3) == (8000, 2000, False)

    print("All tests passed!")
except AssertionError:
    print("Test failed!")