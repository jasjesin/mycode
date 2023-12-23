from backend import validation, user_input_message
user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    #    for days in user_input.split():
    days_n_unit = user_input.split(":")
    days_n_unit_dictionary = {"days": days_n_unit[0], "unit": days_n_unit[1]}
    validation(days_n_unit_dictionary)
