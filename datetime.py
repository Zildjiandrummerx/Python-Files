import datetime

dir(datetime)
# ['__builtins__', '__cached__', '__doc__', '__file__', 
#  '__loader__', '__name__', '__package__', '__spec__', 'datetime']

now = datetime.datetime.now() #Python3
# 2018-10-16 17:50:50.483000 
""" django.utils.timezone.now() #Django 1.4+ """

treehouse_start = datetime.datetime.now()
treehouse_start.replace(hour=9, minute=0, second=0, microsecond=0)
treehouse_start

time_worked = datetime.datetime.now() - treehouse_start
dir(time_worked)

hours_worked = round(time_worked.seconds/3600)
hours_worked

###############################################################################

# Assign datetime to a variable:
now = datetime.datetime.now()
# Move FWD Time by 3 days:
datetime.timedelta(days=3)
datetime.timedelta(3)

now + datetime.timedelta(days=3)
# datetime.datetime(2018, 10, 20, 0, 19, 4, 780064)

now + datetime.timedelta(days=-5)
# datetime.datetime(2018, 10, 12, 0, 21, 17, 934138)

now - datetime.timedelta(days=5)
# datetime.datetime(2018, 10, 12, 0, 21, 17, 934138)

now.date()
# datetime.date(2018, 10, 12, 0)

now.time()
# datetime.time(21, 17, 934138)

hour = datetime.timedelta(hours=1)
hour
# datetime.timedelta(0, 3600)
workday = hour * 9
tomorrow = datetime.datetime.now().replace(hour=9, minute=0) + datetime.timedelta(days=1)
appointment = datetime.timedelta(minutes=45)
start = datetime.datetime(2018, 11, 1, 12, 45)
end = start + appointment

###########################################################################################

#Both return the same. However, ".now" can take timezone as an argument
now = datetime.datetime.now() 
today = datetime.datetime.now() 

today = datetime.datetime.cobine(datetime.date.today(), datetime.time())

##########################################################################################

# strftime - Method to create a string from a datetime
# strptime - Method to create a datetime from a string according to a format string

import datetime
now = datetime.datetime.now()
now.strftime('%B %d')
# 'October 22'
now.strftime('%m/%d/%y')
# '10/22/18'

birthday = datetime.datetime.strptime('2019-10-18', '%Y-%m-%d')
# >>> birthday
# datetime.datetime(2018, 10, 22, 0, 0)
birthday_party = datetime.datetime.strptime('2018-10-22 12:00', '%Y-%m-%d %H:%M')
# >>> birthday_party
# datetime.datetime(2018, 10, 22, 12, 0)
