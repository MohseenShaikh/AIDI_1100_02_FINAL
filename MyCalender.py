# Importing required packages for dealing with dates.
from datetime import datetime, timedelta

# My Calender is the custom class to fetch past dates sequentially.
class MyCalender:
  # Initializer  
  def __init__(self):
    self.dates = []

  # Gets the previous dates according to given param
  # Param: ndays - Number of previous from current date
  # Eg: We need past week's list then pass 7
  # Returns: A list of dates in string format 
  def get_dates_list(self, ndays):
    # Current date
    today = datetime.now()  

    # Calculates Starting date - for this case by subtracting current date with time delta of number of days
    date_week_ago = today - timedelta(days=ndays)

    # Store the list of dates in form of strings
    self.dates=[str((date_week_ago + timedelta(days=i)).date()) for i in range(1,ndays+1)]
    return self.dates