import pygame
class Sprite():
    def __init__(self, width, height, x, y):
        self.coord = x, y
        self.rect = pygame.Rect(x, y, width, height)
        self.s1 = pygame.Surface((width,height))
        self.size = self.define_size()
        self.s1.fill((0, 198,173))
        self.state = 0
    def define_size(self):
        if self.coord[0] == 0:
            size_x = 197
        elif self.coord[0] == 210:
            size_x = 210
        else:
            size_x = 230
        if self.coord[1] == 0:
            size_y = 197
        elif self.coord[1] == 210:
            size_y = 210
        else:
            size_y = 230
        return(size_x, size_y)
    def is_clicked(self):
        x, y = pygame.mouse.get_pos()
        x -= 35
        y -= 35
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint((x, y))
    def x(self):
        pygame.draw.line(self.s1, (30, 30, 30),(75, 135), (135, 75), 20)

        pygame.draw.line(self.s1, (30, 30, 30),(75, 75), (135, 135), 20)
    def circle(self):
        pygame.draw.circle(self.s1, (240, 240, 240),(self.size[0]/2, self.size[1]/2), 60, 10)
    def surface(self):
        return self.s1
    def reset(self):
         self.s1.fill((0, 198,173))