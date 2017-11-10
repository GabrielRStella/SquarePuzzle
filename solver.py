import board, copy, queue

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
        #entry format: error, board, current position, list of moves
        pq.put((board.getError(), PathGroup(board, board.findEmpty(), [])))
        while not pq.empty():
            entry = pq.get()
            group = entry[1]
            print(group.move)
            if(len(group.moves) >= depth):
                for x in group.moves:
                    q.put(x)
                return
            for p in group.board.adj(group.move):
                board2 = group.board.clone()
                board2.swap(group.move, p)
                moves = copy.copy(group.moves)
                moves.append(p)
                pq.put((board2.getError(), PathGroup(board2, p, moves)))

class PathGroup:

    def __init__(self, board, move, moves):
        self.board = board
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
    
