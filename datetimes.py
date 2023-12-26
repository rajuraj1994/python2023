import datetime

date=datetime.datetime.now()
print(date)
# print the year
print(date.year)

# create datetime
date=datetime.datetime(2021,5,20)
print(date)

# strftime -> takes the parameter,format,specify the format of the return string
print(date.strftime('%B'))


date=datetime.datetime.now()
print(date.strftime('%a'))
print(date.strftime('%A'))
# print weekday as a number 0-6 , 0-sunday 6-saturday 
print(date.strftime('%w'))
# %d -> day of the month eg: 1-31
# %b -> name of the month in short eg:Aug,Oct
# %B -> month in full version eg: August,October 
# %m -> month as a number eg:1-12
# %y -> year without century eg: 23
# %Y -> year with century eg: 2023 
# %H -> hour eg:00:23  18
# %I -> hour eg:00:12   06
# %p -> am/pm
# %M -> Minute  eg:00-59
# %S  -> Second  eg: 00-59
# %f -> Microsecond eg: 000000-999999 (100000)


