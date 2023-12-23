from datetime import datetime

user_input = input("Enter Goal separated by colon (:) with a Deadline Date in MM/DD/YYYY format: ")
input_list = user_input.split(":")
goal = input_list[0]
target_date = input_list[1]
deadline = datetime.strptime(target_date, '%m/%d/%Y')
current_time = datetime.today()
time_left = deadline - current_time
hours = int(time_left.total_seconds() / (60*60))
print(f"\nTime left to meet deadline for {goal} : {time_left.days} days or {hours} hours")
