class Game:
    def __init__(self, coins):
        self.coins = coins
    
    def run(self, start, end):
        max_win = 0
        margin = 0
        takeRight = True
        # Do the calculation

        return (max_win, margin, takeRight)

coingame = Game([4, 4, 9, 4, 1, 2, 3])
print(coingame.run(0, 3)) # (13, 5, False)
print(coingame.run(0, 4)) # (12, 2, False)
print(coingame.run(2, 2)) # (9, 9, True)
print(coingame.run(4, 6)) # (4, 2, True)
