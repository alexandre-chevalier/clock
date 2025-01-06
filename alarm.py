from datetime import datetime
import time

hours = ["10","50","20"]

def alarm(time):
    print(time)
    
    hour    = input("enter the hour you want for the alarm ")
    minutes = input("enter the minutes you want for the alarm ")
    seconds = input("enter the seconds you want for the alarm ")
    
    times   = f"{time[0]}:{time[1]}:{time[2]}"
    alarms  = f"{hour}:{minutes}:{seconds}"
    format_alarms = "%H:%M:%S"
    
    current_times   = datetime.strptime(times,format_alarms) 
    alarm_target    = datetime.strptime(alarms, format_alarms)
    print(alarm_target, current_times)

    ##faut il stocker au format heure pour boucler?##
    
    if current_times == alarm_target:
        print(f"il est  bip biiip biiiiip BIIIIIIIIIIIP votre alarme sonne")
    elif current_times != alarm_target:
        print("BOOOOOOOOY")
        
            

alarm(hours)