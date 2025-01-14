from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Save the current date and time
    current_date = datetime.now()
    # Format the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # Print the formatted date and time
    print(f"Current date and time: {formatted_date}")
    return current_date

# Part 2: Calculate a Future Date
def calculate_future_date(current_date):
    # Prompt the user for the number of days to add
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        # Calculate the future date
        future_date = current_date + timedelta(days=number_of_days)
        # Print the future date
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Main function to execute the script
if __name__ == "__main__":
    # Call the function to display the current date and time
    current_date = display_current_datetime()
    # Call the function to calculate and display the future date
    calculate_future_date(current_date)
