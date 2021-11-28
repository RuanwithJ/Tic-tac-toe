from numpy.matrixlib.defmatrix import matrix
from Sprite import Sprite


class Table():
    def __init__(self, width, high):
        self.table_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.table_sprites = self.createSpriteTable(width, high)

    def createSpriteTable(self, w, h):
        m = []
        for i in range(3):
            m.append([])
            for j in range(3):
                sprite = Sprite(w/3, h/3, h/3*j, w/3*i)
                m[i].append(sprite)
        return m
    def reset(self):
        for i in range(3):
            for j in range(3):
                self.table_matrix[i][j] = 0
                self.table_sprites[i][j].reset()
    def check_game_over(self):
        return _check_game_over(self.table_matrix)
    def valid_position(self):
        return _valid_positions(self.table_matrix)
def _check_game_over( matrix):
    # 0 game on
    # 1 x's win
    # 2 circle's win
    # 3 draw
        x1 = 0
        x2 = 0
        y1 = 0
        y2 = 0
        for i in range(3):
            for j in range(3):
                if matrix[i][j] == 1:
                    x1 += 1
                elif matrix[i][j] == 2:
                    y1 +=1
                if matrix[j][i] == 1:
                    x2+=1
                elif matrix[j][i] == 2:
                    y2 +=1
            if y1 == 3 or y2 == 3:
                return 2
            elif x1 == 3 or x2 == 3:
                return 1
            x1 = 0
            x2 = 0
            y1 = 0
            y2 = 0
        x1 = 0
        x2 = 0
        for i in range(3):
            if matrix[i][i] == 1:
                x1 += 1
            elif matrix[i][i] == 2:
                y1 += 1
        if y1 == 3:
            return 2
        elif x1 == 3:
            return 1
        x1 = 0
        y1 = 0
        for i, e in enumerate((2, 1, 0)):
            if matrix[i][e] == 1:
                x1 += 1
            elif matrix[i][e] == 2:
                y1 += 1
        if y1 == 3:
            return 2
        elif x1 == 3:
            return 1
        for i in range(3):
            for j in range(3):
                if(matrix[i][j]==0):
                    return 0
        return 3
def _valid_positions(matrix):
    positions = []
    for i in range(3):
        for j in range(3):
            if matrix[i][j]==0:
               positions.append((i,j))
    return positions
    
