import datetime

pacific = datetime.timezone(datetime.timedelta(hours=-8))
eastern = datetime.timezone(datetime.timedelta(hours=-5))

naive = datetime.datetime(2018, 10, 24, 9)
# >>> naive
# datetime.datetime(2018, 10, 24, 9, 0)

aware = datetime.datetime(2018, 10, 24, 9, tzinfo = pacific)
# >>> aware
# datetime.datetime(2018, 10, 24, 9, 0, tzinfo=datetime.timezone(datetime.timedelta(-1, 57600)))

# naive.astimezone(eastern)
# ValueError: astimezone() cannot be applied to a naive datetime

aware.astimezone(eastern)
# datetime.datetime(2018, 10, 24, 12, 0, tzinfo=datetime.timezone(datetime.timedelta(-1, 68400)))

auckland = datetime.timezone(datetime.timedelta(hours=13))
# >>> aware.astimezone(auckland)
# datetime.datetime(2018, 10, 24, 6, 0, tzinfo=datetime.timezone(datetime.timedelta(0, 46800)))

mumbai = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
# >>> aware.astimezone(mumbai)
# datetime.datetime(2018, 10, 23, 22, 30, tzinfo=datetime.timezone(datetime.timedelta(0, 19800)))

