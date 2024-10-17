import datetime

#using get current time
# my_day = datetime.datetime.now()
# print(my_day)

#set the time hour,min,sec,m_sec
# my_time = datetime.time(12,54,59,87)
# print(my_time)
# print("this is hour: ",my_time.hour)
# print("This is minutes: ",my_time.minute)
# print("This is second: ",my_time.second)
# print("This is microsecond: ",my_time.microsecond)

#set the date in year,month,day
# my_date = datetime.date(2000,10,26)
# print("This is year: ",my_date.year)
# print("This is year: ",my_date.month)
# print("This is year: ",my_date.day)

#get the current date
# print(datetime.date.today())


#using datetime into one module no need to access to packages

from datetime import datetime,date

'''my_profile = datetime(2000,10,26,11,59,45,10)
my_profile_ = my_profile.replace(minute=10)
print(my_profile_)'''

#comapre the two days

# day1 = datetime.today().date()
# day2 = datetime(2000,10,26).date()
# print(day1 - day2)

            # #OR
# day1 = date.today()
# day2 = date(2000,10,26)

# print(day1 - day2)
