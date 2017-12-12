import sys, pygame, game
pygame.init()

size = width, height = 800, 600
bg = 0, 0, 0

screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Square Puzzle")
#TODO: set window icon

game = game.Game(screen)
game.shuffle()

#TODO:
#-have images instead of numbers
#-AI solver

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.mouseButtonDown(screen, event)
        elif event.type == pygame.MOUSEBUTTONUP:
            game.mouseButtonUp(screen, event)
        else:
            pass
            #print(event)

    screen.fill(bg)

    game.draw(screen)
    pygame.display.flip()
