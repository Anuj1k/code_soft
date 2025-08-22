import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()

def is_moves_left(board):
    for row in board:
        if "_" in row:
            return True
    return False

def evaluate(board):
    
    for row in board:
        if row.count(row[0]) == 3 and row[0] != "_":
            return 10 if row[0] == "O" else -10

    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "_":
            return 10 if board[0][col] == "O" else -10

    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "_":
        return 10 if board[0][0] == "O" else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "_":
        return 10 if board[0][2] == "O" else -10

    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)


    if score == 10:
        return score - depth

    if score == -10:
        return score + depth

    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = "O"
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = "_"
        return best

    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = "X"
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = "_"
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                board[i][j] = "O"
                move_val = minimax(board, 0, False)
                board[i][j] = "_"

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

def play_game():
    board = [["_"] * 3 for _ in range(3)]
    print("Tic-Tac-Toe: You are X, AI is O")
    print_board(board)

    for turn in range(9):
        if turn % 2 == 0: 
            while True:
                try:
                    row = int(input("Enter row (0-2): "))
                    col = int(input("Enter col (0-2): "))
                    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == "_":
                        board[row][col] = "X"
                        break
                    else:
                        print("Invalid move, try again!")
                except ValueError:
                    print("Please enter valid numbers!")
        else:  
            print("AI is thinking...")
            row, col = find_best_move(board)
            board[row][col] = "O"

        print_board(board)
        score = evaluate(board)

        if score == 10:
            print("AI Wins! 🤖")
            return
        elif score == -10:
            print("You Win! 🎉")
            return

    print("It's a Draw! 🤝")

play_game()
