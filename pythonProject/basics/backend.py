"""
print(type("Learn Py fastest b4 2024 starts"))
print(type(23))
print(type(23.26))

print("No. of minutes in 20 days: ", 20 * 24 * 60)
print("20 days are", 20 * 24 * 60, "minutes") # to mix n match numbers wid strings
print("30 days are " + str(30 * 24 * 60) + " minutes") # String concatenation
# above one is very common way, that maybe seen in most code
# more elegant way, f means format text & string in correct way
# print(f"50 days are {50 * 24 * 60} minutes")
# above syntax is new addition to python, only works from py 3.6 onwards
"""
to_hours = 24
to_minutes = 24 * 60
to_seconds = 24 * 60 * 60
unit_hours = "hours"
unit_minutes = "minutes"
unit_seconds = "seconds"
user_input_message = "\n*******\nEnter no. of days, separated by colon (:), to compute hours, minutes n seconds for \n"


def days_to_units(num_of_days, unit):
    if unit == "hours":
        print(f"{num_of_days} days are {num_of_days * to_hours} {unit_hours}")
    elif unit == "minutes":
        print(
            f"{num_of_days} days are {num_of_days * to_minutes} {unit_minutes}")
    elif unit == "seconds":
        print(
            f"{num_of_days} days are {num_of_days * to_seconds} {unit_seconds}")
    else:
        print("Incorrect unit specified")
    # print(custom_message)


def validation(days_n_unit_dictionary):
    if days_n_unit_dictionary["days"].isdigit():
        num_of_days = int(days_n_unit_dictionary["days"])
        if num_of_days > 0:
            days_to_units(num_of_days, days_n_unit_dictionary["unit"])
        elif num_of_days == 0:
            print("Enter a positive value for days that is greater than zero")
    else:
        print("Please enter positive integer value")
