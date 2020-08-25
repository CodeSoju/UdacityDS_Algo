#Calculating the number of days between two dates
def daysInMonth(year, month):
    return 30

def nextDay(year, month, day):
    '''Warning: this version assumes all months have 30 days!!!'''
    if day < 30:
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    '''Returns True if year1-month1-day1 is before year2-month2, day2'''
    '''Otherwise, returns False'''
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1 and 
        year2, month2, day2. Assumes inputs are valid dates in Gergorian calendar,
        and the first date is not after the second.
    """
    days = 0
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days
    