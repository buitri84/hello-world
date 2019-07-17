# Declare board, set of winning states, and initialize state vector for each player
board = []
for i in range(9):
    board.append({"occupied": False, "player": 0})
winning = [{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}]
player_x = set()
player_o = set()

# This function checks if a move is legal and updates the board, also updates the state vector of each player, then returns true or false
def move(pos, player):
    if board[pos]["occupied"] == True:
        return False
    else:
        board[pos]["occupied"] = True
        board[pos]["player"] = player
        if player == 1:
            player_x.add(pos)
        elif player == -1:
            player_o.add(pos)
        return True

# This function checks the state of the game and return the score (1 if player 1 wins, -1 if player -1 wins, and 0 if it is a draw or incomplete)
def gameover():
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
        if i["occupied"] == False:
            return False, 0
    return True, 0


def main():
    # Set flag for starting player
    flag = 1
    # Loop to keep getting input where to play
    while True:
        state, score = gameover()
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
            mov = move(pos, flag)
            # if the move has succeded, switch player (flag), otherwise do nothing ie. current player moves again
            if mov == True:
                flag = -1* flag
        print(board)

if __name__ == "__main__":
    main()