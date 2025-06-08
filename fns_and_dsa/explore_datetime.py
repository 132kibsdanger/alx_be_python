from datetime import datetime

def display_current_datetime():
    """Display the current date and time."""
    current_date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"Current Date and Time: {current_date_time}")

def calculate_future_date(number_of_days):
    """Calculate a future date based on the current date."""
    current_date_time = datetime.now()
    future_date = current_date_time +datetime.timedelta(days=number_of_days)
    print (f"Future date: {future_date.strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    display_current_datetime()
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(number_of_days)

if __name__ == "__main__":
    main()