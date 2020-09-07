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

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

teleNums = dict()
timeSpentDuration = 0
longestTimeNumber = None

for i in range(len(calls)):
    teleNums[calls[i][0]] = teleNums.get(calls[i][0], 0) + int(calls[i][-1])
    teleNums[calls[i][1]] = teleNums.get(calls[i][1], 0) + int(calls[i][-1])

    if teleNums[calls[i][0]] > timeSpentDuration:
        longestTimeNumber = calls[i][0]
        timeSpentDuration = teleNums[calls[i][0]]
    if teleNums[calls[i][1]] > timeSpentDuration:
        longestTimeNumber = calls[i][1]
        timeSpentDuration = teleNums[calls[i][1]]

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(longestTimeNumber, timeSpentDuration))

