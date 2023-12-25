def display(board, positions):
    print('Player Board \t Board Positions')
    print(f' {board[1]} | {board[2]} | {board[3]} \t\t   {positions[1]} | {positions[2]} | {positions[3]}')
    print(' --------- \t\t  -----------')
    print(f' {board[4]} | {board[5]} | {board[6]} \t\t   {positions[4]} | {positions[5]} | {positions[6]}')
    print(' --------- \t\t  -----------')
    print(f' {board[7]} | {board[8]} | {board[9]} \t\t   {positions[7]} | {positions[8]} | {positions[9]}')


def data_update(board, position):
    choice = ''
    choice_range = ['X', 'O']
    while choice not in choice_range:
        choice = input("Enter X or O: ").upper()
        if choice not in choice_range:
            print('Invalid input. Enter X or O')
    board[position] = choice
    return choice


def board_position():
    position = ''
    position_range = [x for x in range(1, 10)]
    print(position_range)
    while position not in position_range:
        position = int(input("Enter position 0 to 9 : "))
        if position not in position_range:
            print('Invalid input. Enter position 0 to 9.')
    return position


def new_game():
    usr_input = ''
    input_range = ['Y', 'n']
    while usr_input not in input_range:
        usr_input = input("Want to play new game? (Y/n) : ")
        if usr_input not in input_range:
            print('Invalid input. Enter Y or n')
    if usr_input == 'Y':
        return True
    elif usr_input == 'n':
        print('Thank for playing and have a good time ahead..!!')
        return False


def manipulate_game(board, choice):
    if (board[1] == choice and board[2] == choice and board[3] == choice) or \
            (board[4] == choice and board[5] == choice and board[6] == choice) or \
            (board[7] == choice and board[8] == choice and board[9] == choice) or \
            (board[1] == choice and board[4] == choice and board[7] == choice) or \
            (board[2] == choice and board[5] == choice and board[8] == choice) or \
            (board[3] == choice and board[6] == choice and board[9] == choice) or \
            (board[1] == choice and board[5] == choice and board[9] == choice) or \
            (board[3] == choice and board[5] == choice and board[7] == choice):
        print('You Win..!!')
        return False
    else:
        return True


keep_playing = True

while keep_playing:
    user_input = True
    user_board = [''] * 10
    position_numbers = ['', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print('\n'*10)
    while user_input:
        display(user_board, position_numbers)
        position = board_position()
        choice = data_update(user_board, position)
        display(user_board, position_numbers)
        user_input = manipulate_game(user_board, choice)
    keep_playing = new_game()