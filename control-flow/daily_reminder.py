# daily_reminder.py

# Loop to ensure valid input
while True:
    task = input("Enter your task: ").strip()
    if task:
        break
    print("Task cannot be empty. Please enter a valid task.")

# Loop for valid priority
while True:
    priority = input("Priority (high/medium/low): ").lower().strip()
    if priority in ['high', 'medium', 'low']:
        break
    print("Invalid input. Please enter 'high', 'medium', or 'low'.")

# Loop for valid time-bound input
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
    if time_bound in ['yes', 'no']:
        break
    print("Invalid input. Please enter 'yes' or 'no'.")

# Reminder message initialization
reminder = ""

# Match case for priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Note: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."

# Append time-bound message if applicable
if time_bound == "yes":
    if priority == "low":
        reminder = f"Reminder: '{task}' is a low priority task that still requires immediate attention today!"
    else:
        reminder += " that requires immediate attention today!"

# Print the final message
print("\n" + reminder)
