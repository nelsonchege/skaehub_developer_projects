import numpy as np
# user must specify format
print('Enter year and month you want to count format:2000-04')
start_count = input()
print('Enter same year and the next month format:2000-05 ')
stop_count = input()
# .busday_count() method from numpy gets the number of weekdays
weekday = np.busday_count(start_count, stop_count)
print(weekday)
