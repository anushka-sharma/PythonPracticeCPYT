import calendar
#import datetime
#import time

#print days of a week with defined header length
print(calendar.weekheader(3))
#this number inside weekheader will define length of headers
#in python week starts from Monday, let's print it to remind us of it
print("In python week starts from Monday")
print()
# this blank print is for changing line


print(calendar.firstweekday())
#will print 0, bcs monday is first day and so it is 0,
#and so are days like tuesday=1, wednesday=2
print()


#type in year and month number
print(calendar.month(2020, 4))
print()


#print month in matrix form
print(calendar.monthcalendar(2020, 4))
print()


#to print ENTIRE FREAKING YEAR!
print(calendar.calendar(2020))
#now there's no function to print entire year in matrix form
#what we can do is iterate through eveery month and have to #turn it into matrix form, but thta exercise we'll do later
print()


#will tell you what day it is
#chuck in year, month, day in the same format y-m-d
day_of_the_week=print(calendar.weekday(2020, 4, 27))
print()


#will tell you if the year is leap or not
is_leap=calendar.isleap(2020)
print(is_leap)
#will return true or False
print()


#will tell you number of leap days
#you've to enter from year--to year
how_many_leap_days=calendar.leapdays(2000, 2020)
print(how_many_leap_days)
#this function is inclusve, so if you want to count the leap day of 2020, you've to chuck 2021
print()

