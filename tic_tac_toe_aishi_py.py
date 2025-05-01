import math

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return row[0]

    for col in range(3):
        if all([board[row][col] == board[0][col] != ' ' for row in range(3)]):
            return board[0][col]

    if all([board[i][i] == board[0][0] != ' ' for i in range(3)]) or \
       all([board[i][2 - i] == board[0][2] != ' ' for i in range(3)]):
        return board[1][1]

    if all([cell != ' ' for row in board for cell in row]):
        return 'Tie'
    return None

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif winner == 'Tie':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -math.inf
    move = (0, 0)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    board[move[0]][move[1]] = 'O'

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Tic Tac Toe - You are X, AI is O")
    print_board(board)

    while True:
        # Human move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if board[row][col] != ' ':
            print("Invalid move! Try again.")
            continue
        board[row][col] = 'X'
        print_board(board)

        result = check_winner(board)
        if result:
            print(f"Game Over! {result} wins!" if result != "Tie" else "It's a tie!")
            break

        # AI move
        ai_move(board)
        print("AI's move:")
        print_board(board)

        result = check_winner(board)
        if result:
            print(f"Game Over! {result} wins!" if result != "Tie" else "It's a tie!")
            break

if __name__ == "__main__":
    main()
