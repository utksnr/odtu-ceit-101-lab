'''
#IN THIS ASSIGNMENT YOU WILL WRITE A SIMPLE PROGRAM TO COMPUTE SOMEONE'S AGE IN TERMS OF DAYS AND HOURS. 

STEP-BY-STEP INSTRUCTIONS ARE PROVIDED BELOW.

MAKE SURE THAT THE VARIABLES ARE NAMED PROPERLY.
'''


#1)Define two variables:
#--The first variable should hold the year s/he was born (e.g., 2001)
#--The other variable should hold the current year (i.e., 2021)
year_born = 2001
year_current = 2023

#2)Define two variables:
#--The first variable should hold the month s/he was born (e.g., 9)
#--The other variable should hold the current month (i.e., 12)
#For this assignment, we assume that current month is greater than the month you was born.
month_born = 1
month_current = 10 

#3)Define two variables:
#--The first variable should hold the day you s/he born (e.g., 4)
#--The other variable should hold the current day (i.e., 6)
#For this assignment, we assume that current day is greater than the day you was born.
day_born = 1
day_current = 9

#3)Compute the total number of days that s/he has been alive (in other words, the age in terms of days). 
#Assign the computation result into a new variable. 
#If you have problems with the computation logic, do not hesitate to ask your question in Slack.
years_live = ((year_current - 1) - year_born)
months_live = (month_current-month_born)*30
days_live = day_current - day_born

total_days = (years_live*365) + months_live + days_live

#4)Print the total number of days as shown in the example below.
#The person has been living for 13684 days.
print("The person has been living for "+ str(total_days) + " days.")


#5)Compute the total number of hours that s/he has been alive (in other words, the age in terms of hours). You can use the total number of days to compute the hours easily.
#Assign the computation result into a new variable. 
total_hours = total_days*24

#6)Print the total number of hours as shown in the example below.
#The person has been living for 326496 hours.
print ("The person has been living for "+ str(total_hours) +" hours.")