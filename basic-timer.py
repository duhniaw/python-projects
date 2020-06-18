import time 
import datetime
import re

time_converted = {
"day" : 86400,
"hour" : 3600,
"minute" : 60,
}
def timer():
	confirm_input = input("Set timer for :")
	if confirm_input.endswith("h"):
		fin = re.findall("[0-9]+", confirm_input)
		wait = time_converted["hour"] * int(fin[0])
		time.sleep(wait)
		print("OVER !")
	elif confirm_input.endswith("min"):
		find_minutes = re.findall("[0-9]+", confirm_input)
		wait = time_converted["minute"] * int(find_minutes[0])
		time.sleep(wait)
		print("OVER !")
	elif confirm_input.endswith("d"):
		find_day = re.findall("[0-9]+", confirm_input)
		wait = time_converted["day"] * int(find_day[0])
		print("OVER !")
timer()