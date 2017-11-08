import pygame

class Gui:
    def __init__(self, bounds):
        self.bounds = bounds
        self.elements = []

    def resize(self, bounds):
        pass

    def addElement(self, elem):
        self.elements.add(elem)

    def onClick(self, screen, mouse):
        for x in self.elements:
            if x.contains(mouse):
                x.onClick(screen, mouse)

    def draw(self, screen):
        for x in self.elements:
            x.draw(screen)

class GuiElement:
    def __init__(self, bounds):
        self.bounds = bounds

    def get_rect(self):
        return self.bounds

    #tests if a given point is within this element
    #uses numpy points (tuples)
    def contains(self, pt):
        return self.bounds.collidepoint(pt)

    #click event: mouse = point where mouse is rn
    def onClick(self, screen, mouse):
        pass

    def draw(self, screen):
        pass

class Button(GuiElement):
    def __init__(self, bounds, label, callback):
        super().__init__(bounds)
        self.label = label
        self.callback = callback

    def onClick(self, screen, mouse):
        self.callback(screen, mouse)

    def draw(self, screen):
        screen.fill([0, 0, 0], self.get_rect)
