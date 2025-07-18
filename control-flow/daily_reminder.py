task = input("Enter your task:").strip()

priority = input("Priority (high/medium/low):").strip().lower()

time_bound = input("Is it time-bound? (yes/no):").strip().lower()

priority_description = ""
priority_is_valid = True

match priority:
    case "high":
        priority_description = "a high priority"
    case "medium":
        priority_description = "a medium priority"
    case "low":
        priority_description = "a low priority"
    case _:
        print("Error: Invalid priority entered.")
        priority_is_valid = False

if priority_is_valid:
    if time_bound == "yes":
        print(f"Reminder: '{task}' is {priority_description} task that requires immediate attention today!")
    elif time_bound == "no":
        print(f"Note: '{task}' is {priority_description} task. Consider finishing it when you have free time.")
    else:
        print("Entered an invalid time bound. Please answer 'yes' or 'no'.")