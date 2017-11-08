import board, point, pygame

Point = point.Point
Board = board.Board

class Game:
    def __init__(self, colors):
        self.colors = colors
        self.board = Board(4, 4)
        pass

    def shuffle(self):
        self.board.shuffle()

    def getMenuBounds(self, screen):
        

    def getBoardBounds(self, screen):
        rect = screen.get_rect()
        w = rect.width
        h = rect.height
        dim = min(w, h)
        rect = pygame.Rect((w - dim) / 2, (h - dim) / 2, dim, dim)
        return rect
    
    def draw(self, screen):
        rect = self.getBoardBounds(screen)
        self.drawBoard(screen, rect)

    def drawBoard(self, screen, rect):
        screen.fill(self.colors["bg"], rect)
        board = self.board
        sizex = rect.width / board.width
        sizey = rect.height / board.height
        font = pygame.font.Font(pygame.font.get_default_font(), int(min(sizex, sizey) / 2))
        for i in range(board.size):
            p = board.pointOf(i)
            x = p.x
            y = p.y
            rect2 = pygame.Rect(sizex * x, sizey * y, sizex, sizey)
            rect2.move_ip(rect.x, rect.y)
            rect2.inflate_ip(-15, -15)
            val = board.getAt(p)
            if(val == 0):
                screen.fill(self.colors["btn_empty"], rect2)
            else:
                screen.fill(self.colors["btn"], rect2)
            screen.blit(font.render(str(board.getAt(p)), True, self.colors["text"]), rect2)
            
        
    def getBoardPoint(self, screen, pt):
        rect = self.getBoardBounds(screen)
        board = self.board
        w = board.width
        h = board.height
        x = pt.x - rect.x
        y = pt.y - rect.y
        x = x // (rect.width // board.width)
        y = y // (rect.height // board.height)
        return Point(x, y)
        
    def mouseButtonDown(self, screen, event):
        p = Point(event.pos[0], event.pos[1])
        p = self.getBoardPoint(screen, p)
        #print(p)
        if(not (p is None)):
            board = self.board
            p2 = board.findEmpty()
            if(p in p2.adj()):
                board.swap(p, p2)
        pass

    def mouseButtonUp(self, screen, event):
        #p = Point(event.pos[0], event.pos[1])
        #p = self.getBoardIndex(screen, p)
        pass
