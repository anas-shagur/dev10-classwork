# MATCH HOMEWORK

hours_of_homework = int(input("Hours of homework: "))
day_of_week = int(input("Day of the week [1-7]: "))
due_homework = hours_of_homework > 15

# 1. Re-implement exercise_07 using a match statement.
# Days 6 and 7 represent Saturday and Sunday.
# If it's the weekend and Abdi has less than 15 hours of homework, he skips homework for the day.
# For all other days, or if he has more than 15 hours of homework, he does his homework.
# ---
# You may choose to track data -- maybe a boolean for homework yes/no -- instead of printing a message in
# each case. That's a lot of repeated typing.
# Then print the detailed message after the match.

match day_of_week:
    case 1:
        print("Time to hit those books, buddy.")
    case 2:
        print("Time to hit those books, buddy.")
    case 3:
        print("Time to hit those books, buddy.")
    case 4:
        print("Time to hit those books, buddy.")
    case 5:
        print("Time to hit those books, buddy.")
    case 6:
        if(due_homework):
            print("Time to hit those books, buddy.")
        else:
            print("Yahoo!")
    case 7:
        if(due_homework):
            print("Time to hit those books, buddy.")
        else:
            print("Yahoo!")
    case _:
        print("Invalid day selected.")

