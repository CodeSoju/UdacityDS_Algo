def smallestPositive(in_list):
    smallest_pos = None
    for num in in_list:
        if num > 0:
            if smallest_pos == None or num < smallest_pos:
                smallest_pos = num
    return smallest_pos

def when_offered(courses, course):
    semesters = []
    for semester in courses:
        if course in courses[semester]:
            semesters.append(semester)
    return semesters


'''
Python Functions: returns a value. In case you do not specify a return value explicitly Python 
    will return None from that function 

Generators:
    Similar to a function except instead of returning a value and exiting a process,
    a generator will pause the process, saving its state for next time.
    The biggest difference between a function and generator from a code perspective
    is one word: return is changed to yield

    A generator very useful when dealing with large collections of data that you don't want
    to store in memory all a once. It's also very useful for dealing with extremely large or even
    infinite series

    Example of a generator printing all even numbers:
        Printing all even numbers at once would take an infinite amount of time, but the generator
        allows the process to pause, and go back to creating even numbers when needed. 

        To create the next successive even number simply call next() on the generator object, 
        and it will yield the next iteration. After yield is called, everything in the state
        of the generator function freezes, and the value is returned. When the generator is called 
        agaon with next(), it picks up again with next(), it picks back up right wwhere it stopped
        at yield from before.  
'''

def all_even():
    n = 0 
    while True:
        yield n
        n += 2

my_gen = all_even()

# generate the first 5 even numbers
for i in range(5):
    print(next(my_gen))

# Now go and do some other processing.
do_something = 4
do_something += 3
print(do_something)

# Now go back to generating more even numbers
for i in range(100):
    print(next(my_gen))

def prod(a,b):
    return a*b

def fact_gen():
    i = 1
    n = i 
    while True:
        output = prod(n,i)
        yield output
        i += 1
        n = output 

my_gen = fact_gen()
num = 5
for i in range(num):
    print(next(my_gen))