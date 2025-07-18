# Prompt user for task input
while True:
    task = input("Enter your task: ").strip()
    if task:
        break
    print("Task cannot be empty. Please enter a valid task.")

# Prompt user for priority input
while True:
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority in ["high", "medium", "low"]:
        break
    print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

# Prompt user for time-bound status
while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound in ["yes", "no"]:
        break
    print("Invalid input. Please enter 'yes' or 'no'.")

# Initialize base reminder
reminder = ""

# Use match-case to customize message by priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Note: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."

# Modify message if task is time-bound
if time_bound == "yes":
    # Adjust low-priority message separately to override
    if priority == "low":
        reminder = f"Reminder: '{task}' is a low priority task that still requires immediate attention today!"
    else:
        reminder += " that requires immediate attention today!"

# Print final customized reminder
print("\n" + reminder)