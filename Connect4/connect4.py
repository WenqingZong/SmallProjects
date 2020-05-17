from copy import deepcopy  # To copy a board
import math  # math.inf


def newGame(player1: str, player2: str) -> dict:
    """
    Game constructor, create a new game with the given two players.
    @param: player1 The name of player 1. "C" represents computer.
    @param: player2 The name of player 2. "C" represents computer.
    @return: A dict contains the initial state of the game.
    """
    game = {
        "player1": player1,
        "player2": player2,
        "who": 1,
        "board": [[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0]]
    }
    return game


def checkBoard(board: list) -> None:
    """
    A helper method, to check if the board is valid.
    This method will raise ValueError if the input board is illegal. 
    @param board The game board.
    """
    # Check input is well formed.
    if len(board) != 6:
        raise ValueError("Invalid board! Board is expected to contain 6 rows!")
    for i in range(6):
        if len(board[i]) != 7:
            raise ValueError("Invalid input! Row " + str(i + 1) + " is expected to contain 7 elements!")

    # Check every element is either 0, 1, or 2.
    for i in range(6):
        for j in range(7):
            if board[i][j] != 0 and board[i][j] != 1 and board[i][j] != 2:
                raise ValueError("Board element can only be 0, 1, or 2. It" + " cannot be \"{}\".".format(board[i][j]))


def printBoard(board: list) -> None:
    """
    Print the game board in command line.
    This method will raise ValueError if the input board is not valid.
    """
    checkBoard(board)
    # Print the board.
    print("|1|2|3|4|5|6|7|")
    print("+-+-+-+-+-+-+-+")
    for i in range(6):
        # The leading "|".
        print("|", end = "")
        for j in range(7):
            if board[i][j] == 0:
                print(" |", end = "")
            elif board[i][j] == 1:
                print("X|", end = "")
            else:
                print("O|", end = "")

        # One row finished.
        print()


def getValidMoves(board: list) -> list:
    """
    This method will find all index of colomus which are not filled.
    This method will riase a ValueError if the input board is invalid.
    """
    checkBoard(board)
    validMoves = []

    # A helper method to determine if a column is filled or not.
    def checkFill(board: list, column: int) -> bool:
        return True if board[0][column] == 0 else False

    for i in range(7):
        if checkFill(board, i):
            validMoves.append(i)

    return validMoves


def makeMove(board: list, move: int, who: int) -> list:
    """
    This method assume the move is valid, and return the board after the move.
    @param: board The game board.
    @param: move: Index of which column to insert disk.
    @who: Which player is taking this move.
    """
    try:
        for i in range(7):
            if board[i][move] != 0:
                board[i - 1][move] = who
                break
    except IndexError:
        board[5][move] = who
    return board


def hasWon(board: list, who: int) -> bool:
    """
    Check the given player wons or not.
    """
    # Check horizontal locations for win.
    for column in range(4):
        for row in range(6):
            if board[row][column] == who and board[row][column + 1] == who and \
                    board[row][column + 2] == who and board[row][column + 3] == who:
                return True

    # Check vertical locations for win.
    for column in range(7):
        for row in range(3):
            if board[row][column] == who and board[row + 1][column] == who and \
                    board[row + 2][column] == who and board[row + 3][column] == who:
                return True

    # Check positively diagnal for win.
    for column in range(4):
        for row in range(3):
            if board[row][column] == who and board[row + 1][column + 1] == who \
                    and board[row + 2][column + 2] == who \
                    and board[row + 3][column + 3] == who:
                return True

    # Check negatively diagnal for win.
    for column in range(4):
        for row in range(3, 6):
            if board[row][column] == who and board[row - 1][column + 1] == who \
                    and board[row - 2][column + 2] == who \
                    and board[row - 3][column + 3] == who:
                return True

    # This player is not winning.
    return False


def suggestMove1(board: list, who: int) -> int:
    """
    Suggest a possible move with simple strategy.
    The strategy:
        return if there is an immediate winning move for player who.
        return if a move that can prevent an immediate winning for the other.
        return the first possible move.
    """
    possible_moves = getValidMoves(board)

    # Find if there is an immediate winning move.
    for move in possible_moves:
        copied_board = deepcopy(board)
        copied_board = makeMove(copied_board, move, who)
        if hasWon(copied_board, who):
            return move

    # Prevent an immediate winning move of the other player.
    for move in possible_moves:
        copied_board = deepcopy(board)
        copied_board = makeMove(copied_board, move, 1 if who == 2 else 2)
        if hasWon(copied_board, 1 if who == 2 else 2):
            return move

    # Simplest thought.
    return -1 if len(possible_moves) == 0 else possible_moves[0]


def loadGame(filename: str) -> dict:
    """
    Load a saved game from the file specified.
    This method will raise FileNotFoundError if the required file cannot be
    opened, and raise ValueError if any thing is in a wrong format.
    """

    # Here we assume filename is game.txt if nothing is given.
    # First, we check this file contains exactly 9 lines.
    with open("game.txt" if filename == "" or filename is None else filename, "r") as file:
        for index, line in enumerate(file):
            pass
    if index + 1 != 9:
        raise ValueError("File should contain exactly 9 lines, not " + str(index + 1))

    # Then we read the contents of this file.
    game = {}
    with open("game.txt" if filename == "" or filename is None else filename, "r") as file:
        # Get rid of \n at the end of each line.
        game["player1"] = file.readline()[: -1]
        game["player2"] = file.readline()[: -1]
        game["who"] = int(file.readline())
        if game["who"] != 1 and game["who"] != 2:
            raise ValueError("Value of who can either be 1 or 2, not " + str(game["who"]))

        # Read the board line by line.
        game["board"] = []
        for row in range(6):
            temp = file.readline()[: -1].split(",")
            if len(temp) != 7:
                raise ValueError("A row should contain 7 columns, not " + str(len(temp)))
            for column in range(7):
                temp[column] = int(temp[column])
            game["board"].append(temp)

        # Check the board is correct.
        checkBoard(game["board"])

    return game


def saveGame(game: dict, filename: str = "game.txt") -> None:
    """
    Save the current game to the file specified.
    IOError will be raised if there is anything wrong.
    """
    try:
        with open(filename, "w") as file:
            file.write(game["player1"] + "\n")
            file.write(game["player2"] + "\n")
            file.write(str(game["who"]) + "\n")
            for row in range(6):
                file.write(str(game["board"][row][0]))
                for column in range(1, 7):
                    file.write("," + str(game["board"][row][column]))
                file.write("\n")

        print()
    except IOError as e:
        print("Cannot write to", filename, "\n" + str(e))


def suggestMove2(board: list, who: int) -> int:
    """
    A connect 4 AI.
    This AI is based on adversarial search.
    """

    def score_board(board: list, who: int) -> int:
        """
        Score the next move.
        """

        def score_sub_board(sub_board: list, who: int) -> int:
            """
            Score a sub set of the whole board.
            """
            score = 0
            opponent = 1 if who == 2 else 2
            if sub_board.count(who) == 4:
                score += 100
            elif sub_board.count(who) == 3 and sub_board.count(0) == 1:
                score += 5
            elif sub_board.count(who) == 2 and sub_board.count(0) == 2:
                score += 2

            if sub_board.count(opponent) == 3 and sub_board.count(0) == 1:
                score -= 4

            return score

        score = 0
        # Score centre column.
        centre = [board[i][3] for i in range(6)]
        score += 3 * centre.count(who)

        # Score rows.
        for row_index in range(6):
            row = [board[row_index][i] for i in range(7)]
            for column_index in range(4):
                sub_board = row[column_index: column_index + 4]
                score += score_sub_board(sub_board, who)

        # Score columns.
        for column_index in range(7):
            column = [board[i][column_index] for i in range(6)]
            for row_index in range(3):
                sub_board = column[row_index: row_index + 4]
                score += score_sub_board(sub_board, who)

        # Score positive diagonal.
        for row_index in range(3):
            for column_index in range(4):
                sub_board = [board[row_index + i][column_index + i] for i in range(4)]
                score += score_sub_board(sub_board, who)

        # Score negtive diagonal.
        for row_index in range(3):
            for column_index in range(4):
                sub_board = [board[row_index + 3 - i][column_index + i] for i in range(4)]
                score += score_sub_board(sub_board, who)

        return score

    AI = who
    opponent = 1 if who == 2 else 2

    def minimax(board: list, depth: int, alpha: float, beta: float, maxmize_player: bool) -> (int, int):

        valid_moves = getValidMoves(board)
        game_over = len(valid_moves) == 0 or hasWon(board, 1) or hasWon(board, 2)
        if depth == 0 or game_over:
            if game_over:
                if hasWon(board, AI):
                    return (None, 100000000000000)
                elif hasWon(board, opponent):
                    return (None, -100000000000000)
                else:
                    return (None, 0)
            else:
                return (None, score_board(board, AI))

        # Maximise player score.
        if maxmize_player:
            value = -math.inf
            move = valid_moves[0]
            for valid_move in valid_moves:
                copied_board = deepcopy(board)
                copied_board = makeMove(copied_board, valid_move, AI)
                new_score = minimax(copied_board, depth - 1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    move = valid_move
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return (move, value)

        # Minimise component score
        else:
            value = math.inf
            move = valid_moves[0]
            for valid_move in valid_moves:
                copied_board = deepcopy(board)
                copied_board = makeMove(copied_board, valid_move, opponent)
                new_score = minimax(copied_board, depth - 1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    move = valid_move
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return (move, value)

    return minimax(board, 5, -math.inf, math.inf, True)[0]


def play() -> None:
    """
    Main logic of this game.
    """

    def get_player_name(info: str) -> str:
        """
        This method reads from stdin, and return with the first letter
        capitalised, if user input an empty string, this method will continue
        asking.
        """
        while True:
            name = input(info)
            if name != "":
                return name.title()

    def select_column(game: dict, valid_moves: list) -> int:
        """
        Ask for a column number to select. This method returns a string "s" or
        "S" if the player wants to save the game, otherwise a number between 1
        and 7 which represents the ith column.
        """
        info = (game["player1"] + " (X)" if game["who"] == 1 else game["player2"] + " (O)") + ": Which column to " \
                                                                                              "select? "
        selection = ""
        while True:
            try:
                selection = input(info)
                selection = int(selection)
                if selection - 1 in valid_moves:
                    return selection
                else:
                    print("Invalid input. Try again!")
            except ValueError as e:
                if selection == "s" or selection == "S":
                    saveGame(game)
                    print("The game has been saved to a file.\n")
                else:
                    print("You can only input an integer between 1 and 7.")

    # Print a welcome message to user.
    print("*" * 55)
    print("***" + " " * 11 + "WELCOME TO MY CONNECT FOUR!" + " " * 11 + "***")
    print("*" * 55, "\n")

    print("Enter the player's name, or type \"C\" or \"L\".\n")
    # Ask for player name and create the game dictionary.
    player_name_1 = get_player_name("Name of player 1: ")
    if player_name_1 == "L":
        game = loadGame(input("Please specify the game file name: "))
    else:
        game = newGame(player_name_1, get_player_name("Name of player 2: "))
    print("Okay, let's play!\n")

    # Play the game.
    while True:
        printBoard(game["board"])

        # A draw?
        valid_moves = getValidMoves(game["board"])
        if len(valid_moves) == 0:
            print("A draw")
            return

        # Select a move.
        print()
        if game["player" + str(game["who"])] == "C":
            selection = suggestMove2(game["board"], game["who"]) + 1
            print("Computer", "(X)" if game["who"] == 1 else "(O)", "is thinking... and selected column",
                  str(selection) + ".")
        else:
            selection = select_column(game, valid_moves)
        print()

        # Make the selected move
        game["board"] = makeMove(game["board"], selection - 1, game["who"])

        # Win after move?
        if hasWon(game["board"], game["who"]):
            printBoard(game["board"])
            print((game["player1"] + " (X)" if game["who"] == 1 else game["player2"] + " (O)") + " has won!")
            return

        # Modify the next player.
        game["who"] = 1 if game["who"] == 2 else 2


if __name__ == "__main__":
    play()
