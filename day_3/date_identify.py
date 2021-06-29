import numpy as np
# datetime64() is used to identify time
# when using it will provide the day
# .timedelta64()is used to compliment datetime64()
# snd can be used to know future or past time

# to get the current date
today = np.datetime64('today', 'D')
print("Today is : ", today)
print("+========================+")
# to get the previous day time
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
print("Yesterday was: ", yesterday)
# to get the next time
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("Tomorrow will be: ", tomorrow)
