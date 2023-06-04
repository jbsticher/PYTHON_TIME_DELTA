from datetime import datetime, timedelta

while True:
    try:
        # Get current time and date
        tn = datetime.now()
        # REMOVE THE MILLISECONDS FROM THE OUTPUT
        time_now = tn.replace(microsecond=0)
        # Print current time and date
        print(f'\nThe current time & date is: {time_now}\n')
        # Ask user to input a number of days to calculate a future date
        num_of_days = input('Please input number of days to calculate new date: ')
        print("Do you want to subtract or add day? ('s' or 'a')")
        if not input('> ').lower().startswith('a'):
            future_date = time_now - timedelta(days = int(num_of_days))
            print(f'\nThe date would be: {future_date}')
        else:
            future_date = time_now + timedelta(days = int(num_of_days))
            print(f'\nThe date will be: {future_date}')
        print("\nDo you want to find another day? ('y' or 'n')")
        if not input('> ').lower().startswith('y'):
            break
    # You have to specify the error for Ctrl+C to break the program
    except ValueError:
        print('Sorry, you entered incorrect information. Try again.')

print('\nThank you, have a nice day.\n')



