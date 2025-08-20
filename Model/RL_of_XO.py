import numpy as np

Q = np.load('D:\Q-learningArray.npy')


def if_gameover(board):
    row = np.abs(np.abs(np.sum(board, axis=0))) == 3
    col = np.abs(np.abs(np.sum(board, axis=1))) == 3
    L_dig = np.abs(np.fliplr(board).diagonal().sum()) == 3
    R_dig = np.abs(np.trace(board).sum()) == 3

    if row[0] or row[1] or row[2]:
        index = list(row).index(True)
        player = np.sign(np.sum(board, axis=0))[index]
        return True, player

    elif col[0] or col[1] or col[2]:
        index = list(col).index(True)
        player = np.sign(np.sum(board, axis=1))[index]
        return True, player

    elif L_dig:
        player = np.sign(np.fliplr(board).diagonal().sum())
        return True, player

    elif R_dig:
        player = np.sign(np.trace(board).sum())
        return True, player

    else:
        return False, 0


def Human(board):
    P_ns = np.where(board.ravel() == 0)[0]
    for i in P_ns:
        board_temp = board.copy()
        row, col = divmod(i, 3)
        board_temp[row, col] = -1
        if if_gameover(board_temp)[0]:
            return board_temp
    P_ns = np.random.choice(np.where(board.ravel() == 0)[0])
    row, col = divmod(P_ns, 3)
    board[row, col] = -1
    return board


# helper function for play game
def print_Winner(board):
    if if_gameover(board)[0]:
        if if_gameover(board)[1] == 1:
            print(f"Player X wins!")
        else:
            print(f"Player O wins!")
    else:
        print("Draw!")


# Print the board # helper function for play game
def print_board(board, mood):
    player = 1
    if mood == 1:
        player = -1
    new_arr = np.empty((3, 3), dtype=object)
    for i in range(3):
        for j in range(3):
            if board[i][j] == player:
                new_arr[i][j] = 'X'
            elif board[i][j] == player*-1:
                new_arr[i][j] = 'O'
            else:
                new_arr[i][j] = ' '
    print(new_arr)


# All in one Q
# Set up the Tic Tac Toe board


def AiPlayer(Q, board, player, difficulty_level):
    # Reset the board to start a new game
    board = board

    # while not done:

    # Choose the best action based on the learned Q-table
    state = np.dot(3**np.arange(9), (board.ravel() + 1))
    avi_action = np.where(board.ravel() == 0)[0]

    # np.random.choice(np.where(board.ravel() == 0)[0])
    if difficulty_level == 2:
        action = avi_action[np.argmax(Q[int(state)][avi_action])]
    else:
        action = np.random.choice(avi_action)
    # Update the board with the chosen action
    row, col = divmod(action, 3)
    board[row, col] = player

    '''
            # Check if the game is over
            if if_gameover(board)[0] or (board.ravel() != 0).all():
                done = True
                print_Winner(board)
            else:
                # Switch to the next player
                player *= -1
                x, y = input("enter the position").split()
                while True:
                    if board[int(x)][int(y)] == 0:
                        break
                    else:
                        x, y = input(
                            "This position not empty please ,enter the position again").split()
                board[int(x)][int(y)] = player
                if if_gameover(board)[0] or (board.ravel() != 0).all():
                    done = True
                    print_board(board, mood)
                    print_Winner(board)
                player *= -1
        else:
            print_board(board, mood)
            player *= -1
            x, y = input("enter the position").split()
            while True:
                if board[int(x)][int(y)] == 0:
                    break
                else:
                    x, y = input(
                        "This position not empty please ,enter the position again").split()
            board[int(x)][int(y)] = player
            if if_gameover(board)[0] or (board.ravel() != 0).all():
                done = True
                print_board(board, mood)
                print_Winner(board)
            else:
                # Switch to the next player
                player *= -1
                state = np.dot(3**np.arange(9), (board.ravel() + 1))
                avi_action = np.where(board.ravel() == 0)[0]
                # np.random.choice(np.where(board.ravel() == 0)[0])
                action = avi_action[np.argmax(Q[int(state)][avi_action])]

                # Update the board with the chosen action
                row, col = divmod(action, 3)
                board[row, col] = player

                if if_gameover(board)[0] or (board.ravel() != 0).all():
                    done = True
                    print_board(board, mood)
                    print_Winner(board)
        '''
