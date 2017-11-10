import board, queue

Queue = queue.Queue

class Solver:
    def __init__(self, board, depth):
        self.board = board
        self.depth = depth
        self.reset()
        pass

    #clears the cache of decided moves
    #eg, if the user has changed the board's state
    def reset(self):
        self.q = Queue() # queue of moves
        pass

    #returns the next move in the queue
    def move(self):
        q = self.q
        if q.empty():
            #pass fields as args for convenience
            self.generate(q, self.board, self.depth)
        #just in case...
        if q.empty():
            return None
        return q.get()

    def generate(self, q, board, depth):
        #put crap into queue
        #basically exponentially search for best solution up to a set depth
        #TODO: maybe do it better but probs not huehuehue
        pass
