# explore_datetime.py

from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # save current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # format it nicely
    print("Current date and time:", formatted_date)
    return current_date

# Part 2: Calculate a Future Date
def calculate_future_date(current_date):
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=days_to_add)  # add days
        print("Future date:", future_date.strftime("%Y-%m-%d"))  # format as YYYY-MM-DD
        return future_date
    except ValueError:
        print("Invalid input! Please enter an integer number of days.")

# Main program
if __name__ == "__main__":
    current_date = display_current_datetime()
    calculate_future_date(current_date)
