# Display morning, afternoon, evening or night

import time
timestamp = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
second = int(time.strftime('%S'))

# Display the current time
print("The time is:", timestamp)

# print good morning/evening/afternoon/night
if (hour > 4 and hour <= 12):
    print("Good Morning Sir!")
elif (hour > 12 and hour < 17):
    print("Good Afternoon Sir!")
elif (hour > 17 and hour < 19):
    print("Good Evening Sir!")
elif (hour > 0 and hour <= 4):
    print("Good Night Sir!")
else:
    print("Good Night Sir!")

# End...
