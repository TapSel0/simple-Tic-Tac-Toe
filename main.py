def draw_board():
    for i in range(count_of_cells):
        print_dashes()
        colored_text(f"| {board[i * count_of_cells]} "
                     f"| {board[i * count_of_cells + 1]} "
                     f"| {board[i * count_of_cells + 2]} |")
        print()
    print_dashes()


def take_player_answer():
    while True:
        player_answer = input(f"Where you want put a {player_token}?: ")

        if "0" <= player_answer < "9":
            player_answer = int(player_answer)
            if str(board[player_answer]) not in "XO":
                return player_answer
            else:
                print("This cell is already taken!")
                continue
        else:
            print("Incorrect answer!")


def colored_text(text):
    for i in text:
        if i == "X":
            print("\033[31m{}".format(i), end="")
        elif i == "O":
            print("\033[34m{}".format(i), end="")
        else:
            print("\033[0m{}".format(i), end="")


board = list(range(9))
count_of_cells = 3
print_dashes = lambda: print("-" * 13)

counter = 0
is_win = False
win_cords = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
    (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
)

print("Tic-tac toe the game for two players.")


while not is_win:
    draw_board()

    if counter % 2 == 0:
        player_token = "X"
    else:
        player_token = "O"

    board[take_player_answer()] = player_token

    counter += 1

    if counter > 4:
        for cell in win_cords:
            if board[cell[0]] == board[cell[1]] == board[cell[2]]:
                is_win = True
                break
        if is_win:
            draw_board()
            print(f"{player_token} is win!")
            break
        if counter == 9:
            draw_board()
            print("Draw!")
            break

