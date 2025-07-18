#!/usr/bin/env python3
"""
daily_reminder.py
"""

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

# Determine priority-based message
match priority:
    case "high":
        base_message = f"'{task}' is a high priority task"
    case "medium":
        base_message = f"'{task}' is a medium priority task"
    case "low":
        if time_bound == "yes":
            base_message = f"'{task}' is a low priority task that still requires immediate attention today!"
        else:
            base_message = f"'{task}' is a low priority task. Consider completing it when you have free time."

# Add urgency if time-bound (for high/medium)
if time_bound == "yes" and priority in ["high", "medium"]:
    base_message += " that requires immediate attention today!"

# ✅ Direct print statement starting with Reminder:
print(f"Reminder: {base_message}")
