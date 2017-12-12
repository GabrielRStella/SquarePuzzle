import board, gui, point, pygame, solver

Point = point.Point
Board = board.Board
Solver = solver.Solver

class Game:
    def __init__(self, screen, img):
        self.width = 4
        self.height = 4
        self.solver_depth = 10
        self.txt_board_error = None
        self.img = img
        self.setBoard(self.width, self.height)
        self.colors = {"bg": [0, 0, 0],
                  "btn": [255, 255, 255],
                  "btn_empty": [160, 160, 160],
                  "text": [0, 0, 0]}
        #add menu
        self.gui = gui.Gui(self.getMenuBounds(screen))
        self.gui.addText("Menu:")
        self.txt_width = self.gui.addText("Width: " + str(self.width))
        self.gui.addButton("-", self.cb_decr_width)
        self.gui.addButton("+", self.cb_incr_width)
        self.txt_height = self.gui.addText("Height: " + str(self.height))
        self.gui.addButton("-", self.cb_decr_height)
        self.gui.addButton("+", self.cb_incr_height)
        self.gui.addText("=========")
        self.gui.addButton("Set", self.cb_set)
        self.gui.addButton("Shuffle", self.cb_shuffle)
        self.gui.addText("=========")
        self.gui.addText("Solver")
        self.gui.addButton("Step", self.cb_solver_next)
        self.gui.addButton("Reset", self.cb_solver_reset)
        self.txt_solver_depth = self.gui.addText("Depth: " + str(self.solver_depth))
        self.gui.addButton("-", self.cb_solver_decr_depth)
        self.gui.addButton("+", self.cb_solver_incr_depth)
        self.txt_board_error = self.gui.addText("Error: 0")
        self.updateError()
        
    def cb_decr_width(self, screen, mouse):
        if self.width > 1:
            self.width = self.width - 1
        self.txt_width.label = "Width: " + str(self.width)

    def cb_incr_width(self, screen, mouse):
        self.width = self.width + 1
        self.txt_width.label = "Width: " + str(self.width)

    def cb_decr_height(self, screen, mouse):
        if self.height > 1:
            self.height = self.height - 1
        self.txt_height.label = "Height: " + str(self.height)

    def cb_incr_height(self, screen, mouse):
        self.height = self.height + 1
        self.txt_height.label = "Height: " + str(self.height)

    def cb_set(self, screen, mouse):
        self.setBoard(self.width, self.height)

    def cb_shuffle(self, screen, mouse):
        self.setBoard(self.width, self.height)
        self.shuffle()
        
    def cb_solver_next(self, screen, mouse):
        self.doMove(self.solver.move())
        
    def cb_solver_reset(self, screen, mouse):
        self.solver.reset()

    def cb_solver_decr_depth(self, screen, mouse):
        if self.solver_depth > 1:
            self.solver_depth = self.solver_depth - 1
        self.txt_solver_depth.label = "Depth: " + str(self.solver_depth)
        self.solver = Solver(self.board, self.solver_depth)

    def cb_solver_incr_depth(self, screen, mouse):
        self.solver_depth = self.solver_depth + 1
        self.txt_solver_depth.label = "Depth: " + str(self.solver_depth)
        self.solver = Solver(self.board, self.solver_depth)

    def updateError(self):
        if(self.txt_board_error is not None):
            self.txt_board_error.label = "Error: " + str(self.board.getError())

    def shuffle(self):
        self.board.shuffle(self.width * self.height)
        self.updateError()

    def setBoard(self, w, h):
        self.board = Board(w, h)
        self.solver = Solver(self.board, self.solver_depth)
        self.updateError()
        
    def getMenuBounds(self, screen):
        rect = screen.get_rect()
        width = min(rect.width / 3, 200)
        height = rect.height
        return pygame.Rect(0, 0, int(width), height)

    def getBoardBounds(self, screen):
        rect_menu = self.getMenuBounds(screen)
        rect = screen.get_rect()
        w = rect.width - rect_menu.width
        h = rect.height
        dim = min(w, h)
        rect = pygame.Rect(rect_menu.width + (w - dim) / 2, (h - dim) / 2, dim, dim)
        return rect
    
    def draw(self, screen):
        self.drawBoard(screen, self.getBoardBounds(screen))
        self.drawMenu(screen, self.getMenuBounds(screen))

    def drawBoard(self, screen, rect):
        screen.fill(self.colors["bg"], rect)
        board = self.board
        sizex = rect.width / board.width
        sizey = rect.height / board.height
        font = pygame.font.Font(pygame.font.get_default_font(), int(min(sizex, sizey) / 2))
        img = self.img
        for i in range(board.size):
            p = board.pointOf(i)
            x = p.x
            y = p.y
            rect2 = pygame.Rect(sizex * x, sizey * y, sizex, sizey)
            rect2.move_ip(rect.x, rect.y)
            rect2.inflate_ip(-2, -2)
            val = board.getAt(p)

            p2 = board.pointOf(board.getAt(board.pointOf(i)))
            x = p2.x
            y = p2.y
            rect3 = pygame.Rect(sizex * x, sizey * y, sizex, sizey)
            rect3.inflate_ip(-2, -2)
            screen.blit(img, rect2.topleft, rect3)
            
            if(val == 0):
                screen.fill(self.colors["btn_empty"], rect2)
            #txt = str(board.getAt(p))
            #rect2 = gui.centerText(font.size(txt), rect2)
            #screen.blit(font.render(txt, True, self.colors["text"]), rect2)

    def drawMenu(self, screen, rect):
        font = pygame.font.Font(pygame.font.get_default_font(), self.gui.height() - 2)
        screen.fill([255, 255, 255], rect)
        self.gui.draw(screen, font)
        
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
        if(self.doMove(p)):
            self.solver.reset()
        self.gui.onClick(screen, event.pos)

    def mouseButtonUp(self, screen, event):
        #p = Point(event.pos[0], event.pos[1])
        #p = self.getBoardIndex(screen, p)
        pass

    def doMove(self, p):
        if(not (p is None)):
            board = self.board
            p2 = board.findEmpty()
            if(p in board.adj(p2)):
                board.swap(p, p2)
                self.updateError()
                return True
        return False
        
