import board, copy, queue

Board = board.Board
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
        pq = queue.PriorityQueue()
        startBoard = board
        destBoard = Board(board.width, board.height)
        #entry format: error, current position, list of moves
        pq.put((destBoard.getTotalError(startBoard), PathGroup(startBoard.findEmpty(), [])))
        while not pq.empty():
            entry = pq.get()
            group = entry[1]
            if len(group.moves) >= depth:
                for x in group.moves:
                    q.put(x)
                return
            board2 = startBoard.clone()
            prev = group.move
            for move2 in group.moves:
                board2.swap(prev, move2)
                prev = move2
            for p in board2.adj(group.move):
                board3 = board2.clone()
                board3.swap(group.move, p)
                moves = copy.copy(group.moves)
                moves.append(p)
                pq.put((destBoard.getTotalError(board3), PathGroup(p, moves)))

class PathGroup:

    def __init__(self, move, moves):
        self.move = move
        self.moves = moves

    def __lt__(self, other):
        return False
    
    def __le__(self, other):
        return True
    
    def __eq__(self, other):
        return True
    
    def __ne__(self, other):
        return False
    
    def __gt__(self, other):
        return False
    
    def __ge__(self, other):
        return True

    def __repr__(self):
        return "(" + str(self.move) + ", " + str(self.moves) + ")"
    
