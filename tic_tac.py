import sys
# tic tac toe


# game board
def board(inp):
    """display the game board,
    inp is a list of player moves"""
    val = inp
    print(f"""
        a       b       c
    +-------+-------+-------+   
1   |   {val[0]}   |   {val[1]}   |   {val[2]}   |
    +-------+-------+-------+ 
2   |   {val[3]}   |   {val[4]}   |   {val[5]}   |
    +-------+-------+-------+ 
3   |   {val[6]}   |   {val[7]}   |   {val[8]}   |
    +-------+-------+-------+ 
""")


def game_help_info():
    """displays the game help info to the user"""
    print("""
Help
--------------------------------------------------------------------
This is a 'two' player game!

Use the your keyboard to interact with the game,
during game play enter 'r' to clear the board.
To play use the game board notation 'row x column' to locate each 
move on the board, e.g: 1a .
Enter your moves on the prompt.
if you entre 'm' on prompt it will open the game menu.

Game rule
--------------------------------------------------------------------
Its a two player game, player X and player O

For each move on the broad the player changes.
If a player tries to allocated to a position with value already
assigned the player looses the move and its the other player's turn.

Credit
--------------------------------------------------------------------
Game was made by Peter Kalinde
email to, peterkalinde30@gmail.com for anything with regards to this
game.
--------------------------------------------------------------------
 All rights reserved.
     2022 production.""")
    main_com = input("Enter 'm' for the menu : ")
    print("-" * 68)
    if main_com.lower() == "m":
        game_menu()
    else:
        print("\nPlease enter a valid command\nThan you\n")
        game_help_info()


def pos_move():
    """translate board position notation the index"""
    pos = input("Position: ")
    if pos.lower() == "m":
        game_menu()
    elif pos.lower() == "r":
        game_reset()
    if pos == "1a":
        return 0
    elif pos == "1b":
        return 1
    elif pos == "1c":
        return 2
    elif pos == "2a":
        return 3
    elif pos == "2b":
        return 4
    elif pos == "2c":
        return 5
    elif pos == "3a":
        return 6
    elif pos == "3b":
        return 7
    elif pos == "3c":
        return 8


# store the bata for every move
move_cache = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def move_validation(ind):
    """checks of value of a position"""
    global move_cache
    if move_cache[ind] != " ":
        return False
    else:
        return True


def player_move():
    """"edits the game board"""
    global move_cache

    def action():
        index = pos_move()
        try:
            global move_cache
            if move_validation(index) is True:
                del (move_cache[index])
                move_cache.insert(index, player_turn)
            else:
                print("Position is occupied")
        except:
            if index != ("m" or "r"):
                print("""
Please enter a valid input
use broad notation 'row x column', e.g: 2b
            """)
    action()
    return move_cache


# game logic
count = 1
player_turn = " "


def boo():
    """return boolean 'True' for every
     even value of count, else return force"""
    global count
    count += 1
    if count % 2 == 0:
        return True
    else:
        return False


def player(turn):
    """"turn is "True" for player 'X',
    else player is "O"determine which player's turn"""
    global player_turn
    if turn is True:
        plyer = "X"
    else:
        plyer = "O"
    player_turn = plyer
    print(f"player {plyer}'s turn")


check = True


def winner(move_list):
    """move_list is the list of moves,
    return 'True' if a winner is found,
    else return 'False'"""
    global check
    win = move_list
    # horizontal liniment
    if (win[0] == win[1] == win[2])\
            and (win[0] == win[1] == win[2] != " "):
        if check:
            print(f"Player {win[2]} is the winner")
            check = False
        return True
    elif (win[3] == win[4] == win[5])\
            and (win[3] == win[4] == win[5] != " "):
        if check:
            print(f"Player {win[5]} is the winner")
            check = False
        return True
    elif (win[6] == win[7] == win[8])\
            and (win[6] == win[7] == win[8] != " "):
        if check:
            print(f"Player {win[8]} is the winner")
            check = False
        return True
    # vertical liniment
    elif (win[0] == win[3] == win[6])\
            and (win[0] == win[3] == win[6] != " "):
        if check:
            print(f"Player {win[6]} is the winner")
            check = False
        return True
    elif (win[1] == win[4] == win[7])\
            and (win[1] == win[4] == win[7] != " "):
        if check:
            print(f"Player {win[7]} is the winner")
            check = False
        return True
    elif (win[2] == win[5] == win[8])\
            and (win[2] == win[5] == win[8] != " "):
        if check:
            print(f"Player {win[8]} is the winner")
            check = False
        return True
    # cross liniment
    elif (win[2] == win[4] == win[6])\
            and (win[2] == win[4] == win[6] != " "):
        if check:
            print(f"Player {win[6]} is the winner")
            check = False
        return True
    elif (win[0] == win[4] == win[8])\
            and (win[0] == win[4] == win[8] != " "):
        if check:
            print(f"Player {win[8]} is the winner")
            check = False
        return True
    else:
        return False


def game_reset():
    """reset the game data and clear the board"""
    global move_cache, check
    check = True
    move_cache = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    # show the board before the game starts
    board(move_cache)
    game_play()


def is_board_full(board_value):
    """checks for an empty slot on the board"""
    iterm_list = board_value
    empty = False
    for iterm in iterm_list:
        if iterm == " ":
            empty = True
            # if empty is False at the of
            # iteration the broad is full
            break
    if empty is False:
        print("Board is full\nits a tie")
    return empty


# when a winner is found exit the main loop
game_exit = False


def game_play():
    """control the games main loop"""
    while is_board_full(move_cache)\
            and winner(move_cache) is not True\
            and game_exit is not True:
        # game continues until a winner is
        # found or the board is full
        player(boo())
        board(player_move())
    if winner(move_cache):
        print("""
Enter a command
c - continue game with the board cleared
q - to quit the game
m - for the game menu""")
        win_com = input("enter here : ")
        win_com = win_com.lower()
        if win_com == "c":
            game_reset()
            game_play()
        elif win_com == "q":
            print("""
Exiting 
Thank you for playing the game""")
            sys.exit(0)
        else:
            game_menu()


def game_menu():
    """control the game actions"""
    global game_exit
    print("""
Menu
--------------------------------------------------------------------
Enter the following commands on screen prompt

Commands
  p - to play the game
  q - to quit the game
  h - for help on the rules and to play the game""")
    com = input("Enter a command: ")
    com = com.lower()
    if com == "q":
        print("""
Exiting 
Thank you for playing the game""")
        game_exit = True
        sys.exit(0)
    elif com == "h":
        game_help_info()
    elif com == "p":
        # show the board before the game starts
        board(move_cache)
        game_play()
    else:
        print("Please enter a valid command")
        game_menu()


def main_menu():
    """prompts the user with the game menu"""
    print("""
Welcome to tic tac toe board game 
During play enter m for this menu

Enter a command
p - to start the game 
h - for help with the game
m - for the menu""")
    cm = input("Enter here : ")
    cm = cm.lower()
    if cm == "p":
        # show the board before the game starts
        board(move_cache)
        game_play()
    elif cm == "h":
        game_help_info()
    elif cm == "m":
        game_menu()
    else:
        print("""\nUnknown command prompting help screen\n--->\n""")
        game_help_info()


def main():
    main_menu()


if __name__ == "__main__":
    main()
