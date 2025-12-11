#imported time module 
import time 
#Taking user input in seconds 
user_time=int(input("Enter the time in seconds :")) # we can modify into minutes , hours 
# created a logic using for loop
for x in range (user_time,0,-1):
    seconds= x%60
    minutes= int(x/60 )%60
    hours= int(x/3600)
    print(f"{hours:02} : {minutes:02}  : {seconds:02}")
    #here sleep method slow down the display output 
    time.sleep(1)  # it display multiple outputs for 1 sec lag by one by one 
#final statement 
print("Time is up !!")