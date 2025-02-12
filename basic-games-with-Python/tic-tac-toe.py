import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Initialize board, variables, and scores
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True
score_X = 0
score_O = 0
score_Tie = 0

# Add colors to symbols
def coloredSymbol(symbol):
    if symbol == "X":
        return Fore.BLUE + symbol + Style.RESET_ALL
    elif symbol == "O":
        return Fore.GREEN + symbol + Style.RESET_ALL
    return symbol  # Default for empty spots

# Print the game board
def printBoard(board):
    print(coloredSymbol(board[0]) + " | " + coloredSymbol(board[1]) + " | " + coloredSymbol(board[2]))
    print("----------")
    print(coloredSymbol(board[3]) + " | " + coloredSymbol(board[4]) + " | " + coloredSymbol(board[5]))
    print("----------")
    print(coloredSymbol(board[6]) + " | " + coloredSymbol(board[7]) + " | " + coloredSymbol(board[8]))

# Get player input
def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops, spot is already taken or invalid input!")

# AI makes a random move
def aiMove(board):
    empty_spots = [i for i in range(9) if board[i] == "-"]
    if empty_spots:
        ai_choice = random.choice(empty_spots)
        board[ai_choice] = currentPlayer

# Check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    return False

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    return False

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print(Fore.YELLOW + "It's a tie!" + Style.RESET_ALL)
        gameRunning = False

def checkWin():
    if checkDiag(board) or checkHorizontal(board) or checkRow(board):
        if winner == "X":
            print(Fore.BLUE + f"The winner is {winner}!" + Style.RESET_ALL)
        elif winner == "O":
            print(Fore.GREEN + f"The winner is {winner}!" + Style.RESET_ALL)
        global gameRunning
        gameRunning = False

# Switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# Replay function
def replay():
    play_again = input("Do you want to play again? (Y/N): ").upper()
    if play_again == "Y":
        reset_game()
        return True
    elif play_again == "N":
        print("Thanks for playing!")
        return False
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")
        return replay()

# Reset game function
def reset_game():
    global board, gameRunning, winner, currentPlayer
    board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    gameRunning = True
    winner = None
    currentPlayer = "X"

# Display scores
def displayScores():
    print("\n--- Current Scores ---")
    print(f"Player X: {score_X}")
    print(f"Player O: {score_O}")
    print(f"Ties: {score_Tie}")
    print("----------------------")

# Update scores
def updateScores():
    global score_X, score_O, score_Tie
    if winner == "X":
        score_X += 1
    elif winner == "O":
        score_O += 1
    elif winner is None:
        score_Tie += 1

# Choose game mode
def chooseMode():
    mode = input("Choose mode: 1 for Single-Player, 2 for Two-Player: ")
    if mode == "1":
        return "Single-Player"
    elif mode == "2":
        return "Two-Player"
    else:
        print("Invalid input. Please enter 1 or 2.")
        return chooseMode()

# Main game execution
gameMode = chooseMode()

while True:
    while gameRunning:
        printBoard(board)

        if gameMode == "Single-Player" and currentPlayer == "O":  # AI's turn
            print("AI is making its move...")
            aiMove(board)
        else:  # Human player's turn
            playerInput(board)

        checkWin()
        checkTie(board)

        if not gameRunning:
            updateScores()
            break

        switchPlayer()

    displayScores()
    if not replay():
        break
