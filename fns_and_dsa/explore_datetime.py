#from datetime import datetime, timedelta


# def display_current_datetime():
#     current_date = datetime.now()
#     formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
#     print("Current date and time:", current_date)


# def calculate_future_date():
#     current_date =datetime.now()
#     future_date = current_date + datetime.timedelta(days = number_of_days)
#     print("Future date:", future_date.strftime("%Y-%m-%d"))



# number_of_days = int(input("Enter the number of days to add to the current date:"))

# display_current_datetime()
# calculate_future_date()




from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")


def main():
    display_current_datetime()
    days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(days)

if __name__ == "__main__":
    main()
