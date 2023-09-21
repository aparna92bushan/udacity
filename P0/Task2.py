"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
phone_time = {}
for item in calls:
    if item[0] not in phone_time.keys():
        phone_time[item[0]] = int(item[3])
    elif item[1] not in phone_time.keys():
        phone_time[item[1]] = int(item[3])
    else:
        phone_time[item[0]] += int(item[3])
        phone_time[item[1]] += int(item[3])

max = {}
for k,v in phone_time.items():
    if not max:
        max[k] = v
    else:
        if v > list(max.values())[0]:
            max = {k: v}
print(f"{list(max.keys())[0]} spent the longest time, {list(max.values())[0]} seconds, on the phone during September 2016.")
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

