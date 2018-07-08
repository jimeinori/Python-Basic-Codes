#datetime - to print the date and time in a nice format.
#datetime.now() - to retrieve the current date and time.

#=========================={EXAMPLE}=============================#
from datetime import datetime
now = datetime.now()
print(now)
#========{STORE CURRENT YEAR ONLY INSIDE A NEW VARIABLE}========#
current_year = now.year
#======={STORE CURRENT MONTH ONLY INSIDE A NEW VARIABLE}=======#
current_month = now.month 
#========{STORE CURRENT DAY ONLY INSIDE A NEW VARIABLE}========#
current_day = now.day
#============================{TEST}============================#
print("--------------------------")
print(current_year)
print(current_month)
print(current_day)
#Note: You can also print it directly if you don't need to store it.
print("--------------------------")
print(now.year)
print(now.month)
print(now.day)
#============{PRINT DATE USING FORMAT mm/dd/yyyy}===========#
print("--------------------------")
print("%02d/%02d/%04d" % (now.month, now.day, now.year))
#Check "11-stringmethods.py", line 35, for placeholder recap [%].
#==============={PRINT TIME FORMAT hh:mm:ss}===============#
print("--------------------------")
print("%02d:%02d:%02d" % (now.hour, now.minute, now.second))
#Almost the same with printing date, except we've change the placeholder's padding.
#==============={COMBINING THE TWO AND PRINT}===============#
print("%02d/%02d/%04d %02d:%02d:%02d" % (now.month, now.day, now.year, now.hour, now.minute, now.second))
print("---------------------")
input("Press ENTER to exit.")
