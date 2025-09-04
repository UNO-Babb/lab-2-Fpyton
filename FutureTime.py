#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 5) % 24
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  #Ask user for minutes
  moreMins = 25

  #Calculate the time after the user-supplied time has passed.
  futureMins = (currentMinute + moreMins) % 60
  future_hours = future_hours // 60
  extraHour = (currentMinute + moreMins) // 60
  print(extraHour)
  print(future_hours)
  print(futureMins)
  #Do not use any if statements in calculating the time.

  hour_12 = 9 + 7   
  hour_12 = ((hour_12 - 1) % 12) + 1
  print(hour_12)  

  #Output the future time in standard format "HH:MM"
  add_hours = ("Enter number of hours to add: ")
  add_minutes = ("Enter number of minutes to add: ")

  total_minutes = currentHour * 60 + currentMinute
  add_total_minutes = add_hours * 60 + add_minutes
  
  
  
  #Future Time
  # Convert back to hours and minutes
  future_hours = futureMins // 60
  future_remaining_minutes = futureMins % 60
  # ---- 24-Hour Format ----
  time_24 = "{:02d}:{:02d}".format(future_hours, future_remaining_minutes)
  # ---- 12-Hour Format ----
  hour_12 = ((future_hours - 1) % 12) + 1
  am_pm = "AM" if future_hours < 12 else "PM"
  
  time_12 = "{:02d}:{:02d} {}".format(hour_12, future_remaining_minutes, am_pm) 
  
  
  
  print("Future time will be:")
  print("24-hour format: ", time_24)
  print("12-hour format: ", time_12)

  if __name__ == '__main__': 
    main()
