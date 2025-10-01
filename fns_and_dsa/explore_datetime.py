from datetime import datetime,timedelta
current_date = datetime.now()
def display_current_datetime():
    print("Current date and time: ",current_date) 
def calculate_future_date():
    display_current_datetime()
    number_of_days = int(input("Enter number of days: "))
    future_date = current_date + timedelta(days=number_of_days)
    print("Future date : ",future_date)
    
calculate_future_date()