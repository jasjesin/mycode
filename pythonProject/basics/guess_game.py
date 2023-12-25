from random import shuffle

playlist = ['', 0, '']


def shuffle_list(play_list):
    shuffle(play_list)
    return play_list


def guess_game(location, play__list):
    shuffled_list = shuffle_list(play__list)
    if location > len(play__list) or location == 0:
        return 'Please enter value 1, 2 or 3'
    if shuffled_list[location - 1] == 0:
        return 'Correct'
    else:
        return shuffled_list


number = 1

while number in [1, 2, 3]:
    number = int(input("Guess whether the ball is in 1, 2 or 3 : "))
    print(guess_game(number, playlist))

