import pygame

#return the centered rect
def centerText(size, bounds):
    x = (bounds.width - size[0]) / 2
    y = (bounds.height - size[1]) / 2
    return pygame.Rect(bounds.x + x, bounds.y + y, bounds[0], bounds[1])

class Gui:
    def __init__(self, bounds):
        self.bounds = bounds
        self.elements = []
        self.elemOffset = 0

    def resize(self, bounds):
        for x in self.elements:
            x.bounds.width = bounds.width

    def height(self):
        return 30

    def getElementBounds(self):
        offset = self.elemOffset
        self.elemOffset = offset + 1
        width = self.bounds.width
        height = self.height()
        return pygame.Rect(0, height * offset, width, height)

    def addElement(self, elem):
        self.elements.append(elem)
        return elem

    def addButton(self, label, callback):
        btn = Button(self.getElementBounds(), label, callback)
        self.elements.append(btn)
        return btn

    def addText(self, label, centered = False):
        txt = Text(self.getElementBounds(), label, centered)
        self.elements.append(txt)
        return txt

    def onClick(self, screen, mouse):
        for x in self.elements:
            if x.contains(mouse):
                x.onClick(screen, mouse)

    def draw(self, screen, font):
        for x in self.elements:
            x.draw(screen, font)

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

    def draw(self, screen, font):
        pass

class Button(GuiElement):
    def __init__(self, bounds, label, callback):
        super().__init__(bounds)
        self.label = label
        self.callback = callback
        self.color = (255, 255, 255)

    def onClick(self, screen, mouse):
        self.callback(screen, mouse)
        self.color = (60, 60, 60)

    def draw(self, screen, font):
        screen.fill([0, 0, 0], self.bounds)
        screen.fill(self.color, self.bounds.inflate(-2, -2))
        self.color = ((255 + self.color[0]) / 2, (255 + self.color[1]) / 2, (255 + self.color[2]) / 2)
        screen.blit(font.render(self.label, True, (0, 0, 0)), centerText(font.size(self.label), self.bounds))

class Text(GuiElement):
    def __init__(self, bounds, label, centered = False):
        super().__init__(bounds)
        self.centered = centered
        self.label = label

    def onClick(self, screen, mouse):
        pass

    def draw(self, screen, font):
        rect = self.bounds
        if(self.centered):
            rect = centerText(font.size(self.label), rect)
        screen.blit(font.render(self.label, True, (0, 0, 0)), rect)

