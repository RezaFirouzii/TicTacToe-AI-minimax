# bunch of usefull GUI clesses
# and functions made with pygame 

import pygame


# blits a text on screen
def messageToScreen(screen, message, color, vertical_space=0):
    x, y = screen.get_width() // 2 - len(message) * 6, screen.get_height() // 5 + vertical_space
    font = pygame.font.SysFont('arial', 30, 0, 0)
    text = font.render(message, True, color)
    screen.blit(text, [x, y])


# main board
class Grid:

    def __init__(self, surface, cellSize):
        self.surface = surface
        self.rows = 3
        self.cols = 3
        self.cellSize = cellSize
        self.grid = [([' '] * self.cols) for _ in range(self.rows)]

    # customizing each square based on passed params
    def drawRect(self, pos, value, color):
        row, col = pos
        x, y = col * self.cellSize, row * self.cellSize
        fill, clr = color

        # drawing the rect background
        rect = pygame.Rect(x, y, self.cellSize, self.cellSize)
        self.surface.fill(fill, rect)
        pygame.draw.rect(self.surface, Color.WHITE, rect, 1)

        # drawing label
        indent = ' '
        font = pygame.font.SysFont('arial', 17, True)
        text = font.render(indent + str(row * self.rows + col + 1), True, Color.WHITE)
        self.surface.blit(text, (x + 5, y + 5))

        # drawing value
        font = pygame.font.SysFont('arial', 70, True)
        text = font.render(value, True, clr)
        coord = self.cellSize // 3
        self.surface.blit(text, (x + coord + 10, y + coord - 10))

    # drawing the whole board
    def drawUseRect(self):
        for row in range(self.rows):
            for col in range(self.cols):
                color = ()
                if self.grid[row][col] == 'X':
                    color = (Color.BLACK, Color.BLUE)
                else:
                    color = (Color.BLACK, Color.PINK)
                self.drawRect((row, col), self.grid[row][col], color)


class Color:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 128, 255)
    GREEN = (0, 153, 0)
    YELLOW = (255, 255, 0)
    BROWN = (204, 102, 0)
    PINK = (255, 102, 178)
    PURPLE = (153, 51, 255)
    ORANGE = (255, 117, 56)
    GRAY = (237, 237, 237)

    colors = {
        1: WHITE,
        2: YELLOW,
        3: RED,
        4: BLUE,
        5: GREEN,
        6: BLACK,
        7: BROWN,
        8: PINK,
        9: PURPLE,
    }
