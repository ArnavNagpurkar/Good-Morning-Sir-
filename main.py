# Display morning, afternoon, evening or night

import time
timestamp = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
second = int(time.strftime('%S'))

#Name
name = input("Please enter your name: ")

# Display the current time
print("The time is:", timestamp)

# print good morning/evening/afternoon/night
if (hour > 4 and hour <= 12):
    print("Good Morning",name,"!")
elif (hour > 12 and hour < 17):
    print("Good Afternoon",name,"!")
elif (hour > 17 and hour < 19):
    print("Good Evening",name,"!")
else:
    print("Good Night",name,"!")

# End...
