import board

class Solver:
    def __init__(self, board, depth):
        self.board = board
        self.depth = depth
        self.reset()
        pass

    #clears the cache of decided moves
    #eg, if the user has changed the board's state
    def reset(self):
        self.q = [] # queue of moves
        pass

    #returns the next move in the queue
    def move(self):
        pass
