
# Declare set of winning states
winning = [{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}]

# This function checks if a move is legal and updates the board
def move(board, pos, player):
    if board[pos] != 0:
        return False
    else:
        if player == 1:
            board[pos] = 1
        elif player == -1:
            board[pos] = -1
        return True

# This function checks the state of the game and return the score (1 if player 1 wins, -1 if player -1 wins, and 0 if it is a draw)
# an incomplete game returns False, while completed game returns True
def gameover(board):
    # Create 2 vectors for state of players and populate them
    player_x = set()
    player_o = set()
    for i in range(9):
        if board[i] == 1:
            player_x.add(i)
        elif board[i] == -1:
            player_o.add(i)
    print(player_x)
    print(player_o)
    # Check if any player has winning combination
    for i in winning:
        if i <= player_x:
            return True, 1
        elif i <= player_o:
            return True, -1
    # If not, then it's either just an incomplete game or a draw
    for i in board:
        if i == 0:
            return False, 0
    return True, 0

def main():
    # Declare board. Note: Actually I just need an array, no need for complicated structure
    board = []
    for i in range(9):
        board.append(0)

    # Set flag for starting player
    flag = 1
    # Loop to keep getting input where to play
    while True:
        state, score = gameover(board)
        print(state, score)
        if state == True:
            if score == 1:
                print("Player X wins")
                break
            elif score == -1:
                print("Player O wins")
                break
            elif score == 0:
                print("Draw!!!")
                break
        pos = int(input("Enter the position where you want to make a move: "))
        if pos == -1:
            break
        else:
            mov = move(board, pos, flag)
            # if the move has succeded, switch player (flag), otherwise do nothing ie. current player moves again
            if mov == True:
                flag = -1* flag
        print(board)

if __name__ == "__main__":
    main()
