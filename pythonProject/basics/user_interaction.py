# Getting User Input -- user_choice()
# Creating Functions that edit variables based on user input
#                   -- data_update()
# Generating output -- display_list()
# Joining User Inputs and Logic Flow
def display_list(current_list):
    print('Current setup:\n', current_list)


def user_choice():
    choice = ''
    choice_range = ['0', '1', '2']
    while choice not in choice_range:
        choice = input('Please enter a position 0, 1 or 2 : ')
        if choice not in choice_range:
            print('Invalid choice. Please type position 0, 1 or 2')
    return int(choice)


def data_update(current_list, position):
    new_value = input("Enter new value to replace: ")
    current_list[position] = new_value
    return current_list


def continue_game():
    choice = ''
    choice_range = ['Y', 'n']
    while choice not in choice_range:
        choice = input('Continue Game? (Y/n) : ')
        if choice not in choice_range:
            print('Invalid choice. Please type Y or n')
        elif choice == 'n':
            return False
        else:
            return True


game_list = [0, 1, 2]
game_on = True
while game_on:
    display_list(game_list)
    position = user_choice()
    game_list = data_update(game_list, position)
    display_list(game_list)
    game_on = continue_game()




# ===========================================================
"""
def display(row_1, row_2, row_3):
    print('\n', row_1, row_2, row_3, sep='\n')


def user_choice():
    valid_input = False
    while not valid_input:
        choice = input("Please enter a digit between 1 to 3: ")
        if choice.isdigit():           # 1st check for digit
            if 1 <= int(choice) <= 3:  # 2nd check for value inside range
                valid_input = True
            else:
                print("Input is out of range.")
        else:
            print("Please enter a valid digit (1-3)")


row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']
display(row1, row2, row3)
row2[1] = 'X'
display(row1, row2, row3)
user_choice()
"""