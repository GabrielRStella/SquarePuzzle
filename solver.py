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
        if self.q.empty():
            #pass fields as args for convenience
            self.q = self.generate(self.board, self.depth)
        #just in case...
        if self.q.empty():
            return None
        return self.q.get()

    def generate(self, board, depth):
        #put crap into queue
        #basically exponentially search for best solution up to a set depth
        #TODO: maybe do it better but probs not huehuehue
        pq = queue.PriorityQueue() # Queue()
        startBoard = board
        firstError = startBoard.getError()
        #entry format: error, current position, list of moves
        pq.put((firstError, PathGroup(startBoard.findEmpty(), [])))
        q = Queue()
        while not pq.empty():
            entry = pq.get()
            group = entry[1]
            
            if(entry[0] < firstError):
                q = Queue()
                for x in group.moves:
                    q.put(x)
                if (len(group.moves) >= depth or entry[0] == 0):
                    break
            
            board2 = startBoard.clone()
            prev = group.move
            for move2 in group.moves:
                board2.swap(prev, move2)
                prev = move2
            for p in [x for x in board2.adj(group.move) if (x not in group.moves)]:
                board2.swap(group.move, p) #for calculating error
                moves = copy.copy(group.moves)
                moves.append(p)
                pq.put((board2.getError(), PathGroup(p, moves)))
                board2.swap(group.move, p) #undo previous swap
        return q

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
    
