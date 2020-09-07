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


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

lenTexts = len(texts)
lenCalls = len(calls)
    
answer = set() # Allows for unique elements

i = 0
while i < lenTexts:
    answer.add(texts[i][0])
    answer.add(texts[i][1])
    i += 1
    
j = 0
while j < lenCalls:
    answer.add(calls[j][0])
    answer.add(calls[j][1])
    j += 1

print('There are {} different telephone numbers in the records.'.format(len(answer)))