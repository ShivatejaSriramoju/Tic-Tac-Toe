def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_win(board):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            return board[condition[0]]
    if " " not in board:
        return "Tie"
    return False

def main():
    board = [" "] * 9
    current_player = "X"
    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter your next row and column (1-2-3 and 1-2-3): ")
        try:
            row, col = map(int, move.split())
            if row < 1 or row > 3 or col < 1 or col > 3:
                print("Invalid input. Please enter a number between 1 and 3.")
                continue
            index = (row - 1) * 3 + col - 1
            if board[index] != " ":
                print("Position already occupied. Please choose another one.")
                continue
            board[index] = current_player
            result = check_win(board)
            if result:
                print_board(board)
                if result == "Tie":
                    print("It's a tie!")
                else:
                    print(f"Player {result} wins!")
                break
            current_player = "O" if current_player == "X" else "X"
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")

if __name__ == "__main__":
    main()
1