from MinMax import min_max
import pygame
from Table import Table
from copy import deepcopy
class Game():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.score = [0, 0]
        self.graph_init()
        self.table = Table(630, 630)
    def graph_init(self):
        pygame.init()
        self.width,self.high = (630, 630)
        self.screen = pygame.display.set_mode((630, 630))
    def draw_lines(self):
        line_color = (0,169,147)
        line_width = 20
        pygame.draw.line(self.screen,line_color, (0, 205), (630, 205), line_width)
        pygame.draw.line(self.screen,line_color, (0, 425), (630, 425), line_width)
        pygame.draw.line(self.screen,line_color, (425, 0), (425, 630), line_width)
        pygame.draw.line(self.screen,line_color, (205, 0), (205, 630), line_width)
        
        
    def start(self):
        x_turn = True
        while True:
            state = self.table.check_game_over()
            if(state != 0):
                self.table.reset()
            if(not x_turn):
                position = min_max(deepcopy(self.table.table_matrix))[1]
                y, x = position
                sprite = self.table.table_sprites[y][x]
                sprite.circle()
                self.table.table_matrix[y][x] = 2
                x_turn = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(3):
                        for j in range(3):
                            if(x_turn and self.table.table_matrix[i][j] == 0):
                                sprite = self.table.table_sprites[i][j]
                                if(sprite.is_clicked()):
                                        sprite.x()
                                        self.table.table_matrix[i][j] = 1
                                        x_turn = False

            for i in range(3):
                for j in range(3):
                    self.screen.blit(self.table.table_sprites[i][j].surface(),self.table.table_sprites[i][j].rect)
            self.draw_lines()
            pygame.display.update()
            self.clock.tick(60)
    

        




