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



        # check data structure
        
        # max_left = recurse left
        # max_right = recurse right

        # max += max of max_left and max_right

        # margin +=

        # if max left > max right
        # take_right = false


        # need a base case
        # need data storage structure?

        return (max_win, margin, takeRight)


Game([1,2])