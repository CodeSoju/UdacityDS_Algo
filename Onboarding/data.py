class Person:
    def __init__(self, name, age, month):
        self.name = name
        self.age = age
        self.birthday_month = month
    
    def birthday(self):
        self.age += 1
    
def create_person_objects(names, ages, months):
    my_data = zip(names, ages, months)
    person_objects = []
    for item in my_data:
        person_objects.append(Person(*item))
    return person_objects

def get_april_birthdays(people):
    april_birthdays = {}
    for person in people:
        if person.birthday_month == 'April':
            person.age += 1
            april_birthdays[person.name] = person.age
    return april_birthdays

def get_most_common_month(people):
    months = {'Jan':0, 'Feb':0, 'March':0, 'April':0, 'May':0, 'June':0, 'July':0, 'Aug':0, 'Sept':0, 'Oct':0, 'Nov':0, 'Dec':0}
    for person in people:
        months[person.birthday_month] += 1
    max_month = None
    max_value = 0
    for key in months:
        if months[key] > max_value:
            max_value = months[key]
            max_month = key
    return max_month