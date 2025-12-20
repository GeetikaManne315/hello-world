import time


print("Let's start the countdown")
seconds = int(input("Give us the seconds: "))

while seconds > 0:
    mins , secs = divmod(seconds,60)
    print("Countdown Starts Mins", mins ,"and Seconds ", secs)
    time.sleep(1)
    seconds = seconds - 1
    
print("Times Up!")