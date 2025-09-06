import calendar

def display_calendar():
    while True:
        try:
            year = int(input("Enter year (or 0 to exit): "))
            if year == 0:
                print("Exiting...")
                break
            
            month = int(input("Enter month (1-12): "))
            if month < 1 or month > 12:
                print("Invalid month. Please enter a value between 1 and 12.")
                continue
            
            cal = calendar.TextCalendar(calendar.SUNDAY)  # Week starts on Sunday
            month_calendar = cal.formatmonth(year, month)
            print(month_calendar)
            
        except ValueError:
            print("Invalid input. Please enter a valid number.")

display_calendar()
