
# MODULES
import pygame
import sys
import numpy as np
import RL_of_XO
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from PIL import ImageTk, Image
import sys
# initializes pygame
pygame.init()


mood = 1


# ---------
# CONSTANTS
# ---------
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 11
WIN_LINE_WIDTH = 11
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 126
CIRCLE_RADIUS = 40
CIRCLE_WIDTH = 11
CROSS_WIDTH = 15
SPACE = 30

X_score = 0
O_score = 0

draws_score = 0
hardness = 'Easy'
difficulty_level = 1
# rgb: red green blue
RED = (255, 0, 0)
GREEN = (0, 255, 0)
MENT = (255, 200, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

board = np.zeros((3, 3))

white = (255, 255, 255)
# ------
# SCREEN
# ------
start_flag = 0


def setparameter(event):
    global difficulty_level
    global hardness
    if cmbhoppies.current() == 0:
        difficulty_level = 1
        hardness = 'Easy'
    else:
        difficulty_level = 2
        hardness = 'Hard'


def set_mood():
    global mood
    if RB_value.get() == 0:
        mood = 1

    else:

        mood = 0


def exit_game():
    sys.exit()


def start_game():
    global start_flag
    start_flag = 1
    demo_screen.destroy()


demo_screen = tk.Tk()
demo_screen.title("Demo Sittings")
demo_screen.geometry("400x400")
demo_screen.resizable(width=False, height=False)

screen_width = demo_screen.winfo_screenwidth()
screen_height = demo_screen.winfo_screenheight()

# Calculate x and y coordinates to center the window
x = (screen_width // 2) - (400 // 2)  # replace 400 with your window width
y = (screen_height // 2) - (400 // 2)  # replace 400 with your window height

# Set window geometry
demo_screen.geometry('400x400+{}+{}'.format(x, y))

img = Image.open("D:\BFCAI\XObg3.png")
filename = ImageTk.PhotoImage(img)
background_lable = Label(demo_screen, image=filename)
background_lable.place(x=0, y=0, relwidth=1, relheight=1)


cmd_value = tk.StringVar()
RB_value = tk.IntVar()

Start_Btn = Button(demo_screen, text="Start Game",
                   width="20", command=start_game)
Start_Btn.place(x=170, y=250)
Exit_Btn = Button(demo_screen, text="Exit",
                  width="10", command=exit_game)
Exit_Btn.place(x=310, y=250)
cmbhoppies = ttk.Combobox(demo_screen, values=(
    "Easy", "Hard"), textvariable=cmd_value, state="randomly")
cmbhoppies.place(x=155, y=120)
cmbhoppies.bind("<<ComboboxSelected>>", setparameter)
cmbhoppies.set("Easy")
Rb_for_x = tk.Radiobutton(demo_screen, text="Player X",
                          variable=RB_value, value=0, command=set_mood)
Rb_for_x.place(x=155, y=172)

Rb_for_o = tk.Radiobutton(demo_screen, text="Player O",
                          variable=RB_value, value=1, command=set_mood)

Rb_for_o.place(x=240, y=172)


demo_screen.mainloop()
# --------------------------------------------------------------
if start_flag == 1:
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('TIC TAC TOE')
    screen.fill(BG_COLOR)

    # -------------
    # CONSOLE BOARD
    # -------------
    #board = np.zeros((BOARD_ROWS, BOARD_COLS))

    # ---------
    # FUNCTIONS
    # ---------

    def draw_lines():
        # 1 horizontal
        pygame.draw.line(screen, LINE_COLOR, (111, SQUARE_SIZE+100),
                         (WIDTH-122, SQUARE_SIZE+100), LINE_WIDTH)
        # 2 horizontal
        pygame.draw.line(screen, LINE_COLOR, (111, 2 * SQUARE_SIZE+100),
                         (WIDTH-122, 2 * SQUARE_SIZE+100), LINE_WIDTH)

        # 1 vertical
        pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE+100, 111),
                         (SQUARE_SIZE+100, HEIGHT-133), LINE_WIDTH)
        # 2 vertical
        pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE+100, 111),
                         (2 * SQUARE_SIZE+100, HEIGHT-133), LINE_WIDTH)

    # -----------------------------------------------------------------------------------

    def draw_circle(row, col):
        pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * (SQUARE_SIZE) + (SQUARE_SIZE//2)+100), int(
            row * (SQUARE_SIZE) + (SQUARE_SIZE//2)+100)), CIRCLE_RADIUS, CIRCLE_WIDTH)

    def draw_cross(row, col):
        xRU = int(col * (SQUARE_SIZE) +
                  (SQUARE_SIZE//2)+100)-(SPACE)
        yRU = int(row * (SQUARE_SIZE) +
                  (SQUARE_SIZE//2)+100)+(SPACE)
        xLU = int(col * (SQUARE_SIZE) +
                  (SQUARE_SIZE//2)+100)-(SPACE)
        yLU = int(row * (SQUARE_SIZE) +
                  (SQUARE_SIZE//2)+100)-(SPACE)

        xRD = int(col * (SQUARE_SIZE) +
                  (SQUARE_SIZE//2)+100)+(SPACE)
        yRD = int(row * (SQUARE_SIZE) +
                  (SQUARE_SIZE//2)+100)-(SPACE)
        xLD = int(col * (SQUARE_SIZE) +
                  (SQUARE_SIZE//2)+100)+(SPACE)
        yLD = int(row * (SQUARE_SIZE) +
                  (SQUARE_SIZE//2)+100)+(SPACE)

        pygame.draw.line(screen, CROSS_COLOR,
                         (xRU, yRU), (xRD, yRD), CROSS_WIDTH)
        pygame.draw.line(screen, CROSS_COLOR,
                         (xLU, yLU), (xLD, yLD), CROSS_WIDTH)

    def draw_figures(board, mood):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if mood == 0:
                    if board[row][col] == -1:
                        draw_circle(row, col)
                    elif board[row][col] == 1:
                        draw_cross(row, col)
                else:
                    if board[row][col] == 1:
                        draw_circle(row, col)
                    elif board[row][col] == -1:
                        draw_cross(row, col)

    def mark_square(row, col, player):
        board[row][col] = player

    def available_square(row, col):
        return board[row][col] == 0

    def is_board_full():
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 0:
                    return False

        return True

    def check_win(player, mood):
        # vertical win check
        for col in range(BOARD_COLS):
            if board[0][col] == player and board[1][col] == player and board[2][col] == player:
                draw_vertical_winning_line(col, player, mood)
                return True

        # horizontal win check
        for row in range(BOARD_ROWS):
            if board[row][0] == player and board[row][1] == player and board[row][2] == player:
                draw_horizontal_winning_line(row, player, mood)
                return True

        # asc diagonal win check
        if board[2][0] == player and board[1][1] == player and board[0][2] == player:
            draw_asc_diagonal(player, mood)
            return True

        # desc diagonal win chek
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            draw_desc_diagonal(player, mood)
            return True

        return False

    def draw_vertical_winning_line(col, player, mood):
        global X_score, O_score
        posX = col * SQUARE_SIZE + SQUARE_SIZE//2 + 100
        global win
        if player == 1 and mood == 1:
            color = CIRCLE_COLOR
            win = 0
            O_score += 1
        elif player == -1 and mood == 1:
            color = CROSS_COLOR
            win = 1
            X_score += 1
        elif player == 1 and mood == 0:
            color = CROSS_COLOR
            win = 0
            X_score += 1
        elif player == -1 and mood == 0:
            color = CIRCLE_COLOR
            win = 1
            O_score += 1
        pygame.draw.line(screen, color, (posX, 111),
                         (posX, HEIGHT - 133), LINE_WIDTH)
        winMessage(win)

    def draw_horizontal_winning_line(row, player, mood):
        global X_score, O_score
        posY = row * SQUARE_SIZE + SQUARE_SIZE//2 + 100

        if player == 1 and mood == 1:
            color = CIRCLE_COLOR
            win = 0
            O_score += 1
        elif player == -1 and mood == 1:
            color = CROSS_COLOR
            win = 1
            X_score += 1
        elif player == 1 and mood == 0:
            color = CROSS_COLOR
            win = 0
            X_score += 1
        elif player == -1 and mood == 0:
            color = CIRCLE_COLOR
            win = 1
            O_score += 1

        pygame.draw.line(screen, color, (111, posY),
                         (WIDTH - 133, posY), WIN_LINE_WIDTH)
        winMessage(win)

    def draw_asc_diagonal(player, mood):
        global X_score, O_score
        if player == 1 and mood == 1:
            color = CIRCLE_COLOR
            win = 0
            O_score += 1
        elif player == -1 and mood == 1:
            color = CROSS_COLOR
            win = 1
            X_score += 1
        elif player == 1 and mood == 0:
            color = CROSS_COLOR
            win = 0
            X_score += 1
        elif player == -1 and mood == 0:
            color = CIRCLE_COLOR
            win = 1
            O_score += 1

        pygame.draw.line(screen, color, (118, HEIGHT - 140),
                         (WIDTH - 140, 118), WIN_LINE_WIDTH)
        winMessage(win)

    def draw_desc_diagonal(player, mood):
        global X_score, O_score
        if player == 1 and mood == 1:
            color = CIRCLE_COLOR
            win = 0
            O_score += 1
        elif player == -1 and mood == 1:
            color = CROSS_COLOR
            win = 1
            X_score += 1
        elif player == 1 and mood == 0:
            color = CROSS_COLOR
            win = 0
            X_score += 1
        elif player == -1 and mood == 0:
            color = CIRCLE_COLOR
            win = 1
            O_score += 1
        pygame.draw.line(screen, color, (118, 118),
                         (WIDTH - 140, HEIGHT - 140), WIN_LINE_WIDTH)
        winMessage(win)

    def restart():
        screen.fill(BG_COLOR)
        draw_lines()
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                board[row][col] = 0

    draw_lines()

    def message(msg, color, dim, size, win=0):
        font = pygame.font.SysFont("Gabriola", size)
        if win:
            font.set_bold(True)
        mesg = font.render(msg, True, color)
        screen.blit(mesg, dim)

    def winMessage(win):
        if win == 1:
            message("YOU WON !", GREEN, [105, 250], 100, 1)
        else:
            message("YOU LOST !", RED, [105, 250], 100, 1)
    # ---------
    # VARIABLES
    # ---------
    player = 1
    game_over = False

    # --------
    # MAINLOOP
    # --------
    if mood:
        player = -1
    else:
        player = 1

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if not game_over:
                if player == -1:
                    if event.type == pygame.MOUSEBUTTONDOWN:

                        mouseX = event.pos[0]  # x
                        mouseY = event.pos[1]  # y
                        if mouseX >= 111 and mouseX <= WIDTH-122 and mouseY >= 111 and mouseY <= HEIGHT-122:

                            clicked_row = int((mouseY-100) // SQUARE_SIZE)

                            clicked_col = int((mouseX-100) // SQUARE_SIZE)

                            if available_square(clicked_row, clicked_col):

                                mark_square(clicked_row, clicked_col, player)

                                draw_figures(board, mood)
                                if RL_of_XO.if_gameover(board)[0] or (board.ravel() != 0).all():
                                    check_win(player, mood)
                                    if RL_of_XO.if_gameover(board)[0] == False and (board.ravel() != 0).all():
                                        draws_score += 1
                                        message("DRAWS !", MENT, [
                                                150, 250], 100, 1)
                                    game_over = True
                                player *= -1
                else:
                    RL_of_XO.AiPlayer(RL_of_XO.Q, board,
                                      player, difficulty_level)

                    draw_figures(board, mood)
                    if RL_of_XO.if_gameover(board)[0] or (board.ravel() != 0).all():
                        check_win(player, mood)
                        if RL_of_XO.if_gameover(board)[0] == False and (board.ravel() != 0).all():
                            draws_score += 1
                            message("DRAWS !", MENT, [
                                    150, 250], 100, 1)
                        game_over = True
                    player *= -1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    board = np.zeros((3, 3))
                    restart()
                    if mood:
                        player = -1
                    else:
                        player = 1
                    game_over = False
        if mood == 1:
            message("You", CROSS_COLOR, [30, 200], 30)
            message("AI", CIRCLE_COLOR, [525, 200], 30)
            message(f"{X_score}", CROSS_COLOR, [35, 280], 40)
            message(f"{O_score}", CIRCLE_COLOR, [530, 280], 40)

        else:
            message("AI", CROSS_COLOR, [35, 200], 30)
            message("You", CIRCLE_COLOR, [520, 200], 30)
            message(f"{X_score}", CROSS_COLOR, [35, 280], 40)
            message(f"{O_score}", CIRCLE_COLOR, [530, 280], 40)

        message("ENJOY YOUR TIME! IN TIC TAC TOE", white, [62, 25], 40)
        message("Player X", CROSS_COLOR, [10, 240], 30)
        message("Player O", CIRCLE_COLOR, [500, 240], 30)
        message(f"It is a {hardness} Mood", CIRCLE_COLOR, [20, 500], 25)
        message("Click on Ctrl+R to play again", CIRCLE_COLOR, [20, 540], 25)
        message("Draws!", MENT, [480, 500], 30)
        message(f"{draws_score}", MENT, [505, 540], 40)

        pygame.display.update()
else:
    sys.exit()
