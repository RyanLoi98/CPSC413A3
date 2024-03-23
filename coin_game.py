import numpy as numpy
class Game:
    # initialization function
    def __init__(self, coins):
        # initialize coin array
        self.coins = coins
        # variable n for length of coin array + 1, this will be the size of column and rows of our 2-D array.
        n = len(coins) + 1
        # use numpy to create n x n 2-D array initialized to -1. This will be used as the data structure to hold
        # previously calculated sub-problems and avoid having to recalculate them
        self.dataStruct = -1 * numpy.ones((n, n))


    def run(self, start, end):
        max_win = 0
        margin = 0
        takeRight = True
        # Do the calculation

        # base case when there are no coins left
        if(len(self.coins) == 0):
            # max_win will be 0, margin will be 0, and takeRight = true by default
            return (max_win, margin, takeRight)

        # base case when there start index = end index
        elif (start == end):
            # max_win will be the value of this last coin
            max_win += self.coins[start]
            # margin will be the value of this lat coin
            margin += self.coins[start]
            # return max_win, margin, and takeRight = true by default
            return (max_win, margin, takeRight)


        # check data structure, if at this start and end index it isn't -1 then it has a previous calculated value
        # so we will utilize this value
        if(self.dataStruct[start][end] != -1):
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
        if(LOppLeft < LOppRight):
            # left margin is the left coin value - the opponent's left coin
            Lmargin = leftCoinValue - self.coins[start + 1]
            # value of recursing left is now based on the min array LOppLeft
            left = LOppLeft + leftCoinValue

        # if LOppLeft >= LOppRight we will take LOppRight, especially when both are equal because we take right by default
        else:
            # left margin is the left coin value - the opponent's right coin
            Lmargin = leftCoinValue - self.coins[end]
            # value of recursing left is now based on the min array LOppRight
            left = LOppRight + leftCoinValue


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
        if (ROppLeft < ROppRight):
            # Right margin is the Right coin value - the opponent's left coin
            Rmargin = RightCoinValue - self.coins[start + 1]
            # value of recursing right is now based on the min array ROppLeft
            right = ROppLeft + RightCoinValue

        # if ROppLeft >= ROppRight we will take ROppRight, especially when both are equal because we take right by default
        else:
            # Right margin is the Right coin value - the opponent's right coin
            Rmargin = RightCoinValue - self.coins[end-1]
            # value of recursing right is now based on the min array ROppRight
            right = ROppRight + RightCoinValue




        # store recursive data into data structure
        self.dataStruct[start][end] = (max_win, margin, takeRight)



        # margin is value of our coin - value of the coin opponent picks to minimize our score

        # max += max of max_left and max_right

        # if max left > max right
        # take_right = false



        # store data into data structure

        return (max_win, margin, takeRight)


Game([1,2])