import os
import optimal_move
from pygame_utils import *

# GUI Constants
TITLE = 'AI plays Tic Tac Toe'
WINDOWS_LOCATION = '350,70'
SIZE = 3
WIDTH = 500
HEIGHT = 500
FPS = 10


# setting the specified square's value to 'X'
def setValue(grid, pos):
    x, y = pos
    if grid.grid[x][y] == ' ':
        grid.grid[x][y] = 'X'
        return 2
    return 1


def run_game():
    CELL_SIZE = HEIGHT // SIZE
    grid = Grid(surface=screen, cellSize=CELL_SIZE)

    winner = 1      # 1 if player wins, -1 if bot wins and 0 for tie
    turn = 1        # 1 if player starts first otherwise 2
    running = True
    while running:
        clock.tick(FPS)

        screen.fill(Color.BLACK)
        messageToScreen(screen, "Welcome to Tic Tac Toe with BOT !", Color.WHITE, -50)
        messageToScreen(screen, "Who starts first?", Color.WHITE, 50)
        messageToScreen(screen, "1) ME ", Color.BLUE, 125)
        messageToScreen(screen, "2) BOT", Color.PINK, 175)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    turn = 1
                    running = False
                elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    turn = 2
                    running = False

    if turn == 2:
        grid.grid[0][0] = 'O'
        turn = 1

    # game loop
    running = True
    while running:
        clock.tick(FPS)

        winner = optimal_move.isFinished(grid.grid) // optimal_move.MIN_SCORE
        if winner or not optimal_move.moveLeft(grid.grid):
            pygame.time.wait(750)
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            # player's turn
            if turn == 1:
                # setting the value of each sqaure based on 
                # the pressed square number (top left label) on keyboard
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        turn = setValue(grid, (0, 0))
                    elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        turn = setValue(grid, (0, 1))
                    elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                        turn = setValue(grid, (0, 2))
                    elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                        turn = setValue(grid, (1, 0))
                    elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                        turn = setValue(grid, (1, 1))
                    elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                        turn = setValue(grid, (1, 2))
                    elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                        turn = setValue(grid, (2, 0))
                    elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                        turn = setValue(grid, (2, 1))
                    elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                        turn = setValue(grid, (2, 2))

            # AI's turn
            else:
                # kicking off the minimax by computing optimal move
                try:
                    pygame.time.wait(600)
                    x, y = optimal_move.getOptimalMove(grid.grid)
                    grid.grid[x][y] = 'O'
                    turn = 1
                except ValueError:
                    break

            screen.fill(Color.BLACK)
            grid.drawUseRect()
            pygame.display.flip()

    # ending menu
    running = True
    while running:
        clock.tick(FPS)

        if winner == 1:
            message = "Congratulations! You've defeated AI"
            color = Color.GREEN
        elif winner == -1:
            message = "AI defeated you!"
            color = Color.RED
        else:
            message = "Tie!"
            color = Color.WHITE

        screen.fill(Color.BLACK)
        messageToScreen(screen, message, color, -50)
        messageToScreen(screen, "1) Play again", Color.WHITE, 125)
        messageToScreen(screen, "2) Exit      ", Color.RED, 175)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    run_game()
                    running = False
                elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    running = False


if __name__ == "__main__":
    # setting Pygame window position
    os.environ['SDL_VIDEO_WINDOW_POS'] = WINDOWS_LOCATION

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    run_game()

    pygame.quit()
