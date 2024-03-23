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
        if((start > end) or (end < start)):
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
            # left margin is the left coin value - the opponent's left coin
            Lmargin = leftCoinValue - self.coins[start + 1]
            # value of recursing left is now based on the min array LOppLeft
            left = LOppLeft[maxWinIndex] + leftCoinValue

        # if LOppLeft >= LOppRight we will take LOppRight, especially when both are equal because we take right by default
        else:
            # left margin is the left coin value - the opponent's right coin
            Lmargin = leftCoinValue - self.coins[end]
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
            # Right margin is the Right coin value - the opponent's left coin
            Rmargin = RightCoinValue - self.coins[start + 1]
            # value of recursing right is now based on the min array ROppLeft
            right = ROppLeft[maxWinIndex] + RightCoinValue

        # if ROppLeft >= ROppRight we will take ROppRight, especially when both are equal because we take right by default
        else:
            # Right margin is the Right coin value - the opponent's right coin
            Rmargin = RightCoinValue - self.coins[end - 1]
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



coingame = Game([4, 4, 9, 4, 1, 2, 3])
print(coingame.run(0, 3)) # (13, 5, False)
print(coingame.run(0, 4)) # (12, 2, False)
print(coingame.run(2, 2)) # (9, 9, True)
print(coingame.run(4, 6)) # (4, 2, True)

