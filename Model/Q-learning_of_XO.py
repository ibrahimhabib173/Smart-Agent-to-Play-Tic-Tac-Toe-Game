import numpy as np


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


board = np.zeros((3, 3))


def q_learning(board):
    epsilon = 0.1
    gamma = 0.9
    alpha = 0.5
    episodes = 100000

    # Initialize the Q-table with zeros

    Ai_player = 1  # player X for case 1
    Ai_player2 = 1  # player O for case 2

    for i in range(episodes):
        if i % 5000 == 0:
            print(i)
    # Initialize state for case 1 AI start the game ------------------------------------------
        flag = 0
        board = np.zeros((3, 3))
        reward = 0

        # Initialize state for case 2

        init_board = board

        state = np.dot(3**np.arange(9), (init_board.ravel() + 1))

        init_action = np.random.randint(9)
        row, col = divmod(init_action, 3)
        board[row, col] = Ai_player
        action = init_action
    # --------------------------------------------------------------------------------------------
    # Initialize state for case 2 human start the game ------------------------------------------

        flag2 = 0
        board2 = np.zeros((3, 3))
        reward2 = 0

        # Initialize state for case 2

        board2 = Human(board2)

        state2 = np.dot(3**np.arange(9), (board2.ravel() + 1))
        action2 = np.random.choice(np.where(board2.ravel() == 0)[0])

    # -------------------------------------------------------------------------------------------
        while True:  # loob for case 1

            if if_gameover(board)[0] or (board.ravel() != 0).all():

                # Player 1 wins (+1) or Player 2 wins (-1) or draw (0)
                reward = if_gameover(board)[1]
                flag = 1
            else:
                board = Human(board)
                reward = 0

                if if_gameover(board)[0] or (board.ravel() != 0).all():

                    # Player 1 wins (+1) or Player 2 wins (-1) or draw (1)
                    reward = if_gameover(board)[1]
                    flag = 1

            # Update the Q-table based on the Bellman equation
            next_state = np.dot(3**np.arange(9), (board.ravel() + 1))
            Q[int(state)][action] += alpha * (reward + gamma *
                                              np.max(Q[int(next_state)]) - Q[int(state)][action])
            state = next_state

            if flag == 1:
                break

            if np.random.uniform() < epsilon:
                # Explore: choose a random empty cell
                action = np.random.choice(np.where(board.ravel() == 0)[0])
            else:
                # Exploit: choose the best action based on Q-table
                action = np.argmax(Q[int(state)])

            #action = np.random.choice(np.where(board.ravel() == 0)[0])
            row, col = divmod(action, 3)
            board[row, col] = Ai_player

    # -------------------------------------------------------------------------------------------
        while True:  # loob for case 2

            row, col = divmod(action2, 3)
            board2[row, col] = Ai_player2

            if if_gameover(board2)[0] or (board2.ravel() != 0).all():

                # Player 1 wins (+1) or Player 2 wins (-1) or draw (0)
                reward2 = if_gameover(board2)[1]
                flag2 = 1
            else:

                board2 = Human(board2)
                reward2 = 0

                if if_gameover(board2)[0] or (board2.ravel() != 0).all():

                    # Player 1 wins (+1) or Player 2 wins (-1) or draw (1)
                    reward2 = if_gameover(board2)[1]
                    flag2 = 1

            # Update the Q-table based on the Bellman equation
            next_state2 = np.dot(3**np.arange(9), (board2.ravel() + 1))
            Q[int(state2)][action2] += alpha * (reward2 + gamma *
                                                np.max(Q[int(next_state2)]) - Q[int(state2)][action2])
            state2 = next_state2

            if flag2 == 1:
                break
            if np.random.uniform() < epsilon:
                # Explore: choose a random empty cell
                action2 = np.random.choice(np.where(board2.ravel() == 0)[0])
            else:
                # Exploit: choose the best action based on Q-table
                action2 = np.argmax(Q[int(state2)])
            #action2 = np.random.choice(np.where(board2.ravel() == 0)[0])

        # END ----------------------------------------------------------------------------------

    return Q


Q = np.zeros((3**9, 9))
Q = q_learning(board)

np.save('D:\Q-learningArrayUpdate.npy', Q)
