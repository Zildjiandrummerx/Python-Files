"""jramirez@UbuntuAMD64:~/Documents/Python-Files$ python
Python 2.7.15rc1 (default, Apr 15 2018, 21:51:34)
[GCC 7.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information. """
>>> import datetime
>>> import pytz
>>> pacific = pytz.timezone('US/Pacific')
>>> eastern = pytz.timezone('US/Eastern')
>>> fmt = '%Y-%m-%d %H:%M:%S %Z%z'
>>> utc = pytz.utc
>>> start = pacific.localize(datetime.datetime(2018, 10, 25, 9))
>>> start.strftime(fmt)
'2018-10-25 09:00:00 PDT-0700'
>>> start_eastern = start.astimezone(eastern)
>>> start_eastern
datetime.datetime(2018, 10, 25, 12, 0, tzinfo=<DstTzInfo 'US/Eastern' EDT-1 day, 20:00:00 DST>)
>>> start
datetime.datetime(2018, 10, 25, 9, 0, tzinfo=<DstTzInfo 'US/Pacific' PDT-1 day, 17:00:00 DST>)
>>> start_utc = datetime.datetime(2018, 10, 25, 1, tzinfo=utc)
>>> start_utc.strftime(fmt)
'2018-10-25 01:00:00 UTC+0000'
>>> start_pacific = start_utc.astimezone(pacific)
>>> start_pacific
datetime.datetime(2018, 10, 24, 18, 0, tzinfo=<DstTzInfo 'US/Pacific' PDT-1 day, 17:00:00 DST>)
>>> auckland = pytz.timezone('Pacific/Auckland')
>>> mumbai = pytz.timezone('Asia/Calcutta')
>>>
KeyboardInterrupt
>>> apollo_13_naive = datetime.datetime(1970, 4, 11, 14, 13)
>>> apollo_13_eastern = eastern.localize(apollo_13_naive)
>>> apollo_13_naive
datetime.datetime(1970, 4, 11, 14, 13)
>>> apollo_13_eastern
datetime.datetime(1970, 4, 11, 14, 13, tzinfo=<DstTzInfo 'US/Eastern' EST-1 day, 19:00:00 STD>)
>>> apollo_13_utc = apollo_13_eastern.astimezone(utc)
>>> apollo_13_utc.astimezone(pacific).strftime(fmt)
'1970-04-11 11:13:00 PST-0800'


# Format string
fmt = '%Y-%m-%d %H:%M:%S %Z%z'