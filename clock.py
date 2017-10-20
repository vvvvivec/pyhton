# Talking clock
#
# This applet tells you the time, IN ENGLISH!
#
# Amazing, no?
#
# Gets system time , e.g. 13:05, and returns it in english , e.g. "It is One O' Five"

# Package imports
from datetime import datetime # Supports time gathering
import sys # for sys.exit

# Get the time
time = datetime.now().time()

# Pull out the hour and minute
hour = time.hour
minute = time.minute

# If it's 1300 or later, convert to 12 and under
if (hour > 12):
    hour -= 12

# Define numbers dictionary
number_words = {
    0: None,
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "fourty",
    50: "fifty",
    60: None
}

# Store word equivalent of digit for hour output
hour_out = number_words[hour]

# Determine if minute is under 10 and set "o'" if necessary
if (minute == 0 or minute == 60):
    middle = " o'clock"
elif (minute > 0 and minute < 10):
    middle = " o' "
elif (minute >= 10 and minute < 60):
    middle = " "

# Store word equivalent od digit for minute output
# Note to self: hardcoding this is going to suck
temp_minute = minute # store original minute in case it's needed later
prefix = None # init var for prefix
minute_out = None # init var for final minute_out
if (minute > 0 and minute < 20):
    minute_out = number_words[minute]
elif (minute == 20 or minute == 30 or minute == 40 or minute == 50):
    minute_out = number_words[minute]
elif (minute > 20 and minute < 30):
    prefix = "twenty-"
    minute = minute - 20
    minute_out = prefix + number_words[minute]
elif (minute > 30 and minute < 40):
    prefix = "thirty-"
    minute = minute - 30
    minute_out = prefix + number_words[minute]
elif (minute > 40 and minute < 50):
    prefix = "fourty-"
    minute = minute - 40
    minute_out = prefix + number_words[minute]
elif (minute > 50 and minute < 60):
    prefix = "fifty-"
    minute = minute - 50
    minute_out = prefix + number_words[minute]

# Print the goddamn time
if (minute_out != None):
    print("It is " + hour_out + middle + minute_out + ".")
else:
    print("It is " + hour_out + middle)

# Cleanly exit the program
sys.exit(0)
