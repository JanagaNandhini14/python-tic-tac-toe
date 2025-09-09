# tic_tac_toe.py
def print_board(b):
    print()
    for i in range(3):
        print(" " + " | ".join(b[i*3:(i+1)*3]))
        if i < 2:
            print("---+---+---")
    print()

def check_winner(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b2,c in wins:
        if b[a] == b[b2] == b[c] and b[a] != ' ':
            return b[a]
    if ' ' not in b:
        return "Draw"
    return None

def main():
    board = [' '] * 9
    current = 'X'
    while True:
        print_board(board)
        move = input(f"Player {current}, enter position (1-9): ")
        if not move.isdigit() or not 1 <= int(move) <= 9:
            print("Invalid input. Enter 1-9.")
            continue
        pos = int(move) - 1
        if board[pos] != ' ':
            print("Spot taken. Try another.")
            continue
        board[pos] = current
        result = check_winner(board)
        if result:
            print_board(board)
            if result == "Draw":
                print("It's a draw!")
            else:
                print(f"Player {result} wins!")
            break
        current = 'O' if current == 'X' else 'X'

if __name__ == "__main__":
    main()
