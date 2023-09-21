"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
all_texts_numbers = [x[0] for x in texts ] + [x[1] for x in texts]
all_call_numbers = [x[0] for x in calls ] + [x[1] for x in calls]
callers_without_sms = set(all_call_numbers) - set(all_texts_numbers)
all_incoming_nums = [x[1] for x in calls]
callers_wo_incoming = callers_without_sms - set(all_incoming_nums)
callers_wo_incoming = list(callers_wo_incoming)
callers_wo_incoming.sort()

print("These numbers could be telemarketers: ")
for num in callers_wo_incoming:
    print(num)
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

