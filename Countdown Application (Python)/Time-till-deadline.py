import datetime

user_input = input("Enter your goal with a deadline separated by a colon eg. Learn Python:2.12.2022\n ")
# Splitting the user input with a colon
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()

#Calculating how many days from now till deadline

days_remaining = deadline_date - today_date 

print(f"Time remaining for you to achieve your {goal} goal is {days_remaining.days} days")