import calendar
import os
import argparse

cwd = os.getcwd()

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-y", "--year", required=False, default=2020,
    help="year")
ap.add_argument("-m", "--month", required=False, default=1,
    help="month")

try:
    args = vars(ap.parse_args())
    input_year = int(args['year'])
    input_month = int(args['month'])

    #Print the calendar for input year and month
    print(calendar.month(input_year, input_month))
    
except:
    print("\nPlease enter a valid year and month(1-12)")