def current_date():
    current_year = 2023
    current_month = 10
    current_day = 10
    return current_year, current_month, current_day

def days_live(born_year ,born_moth, born_day):
    current_year, current_month, current_day = current_date()
    diff_y = current_year - born_year
    diff_m = current_month - born_moth
    diff_d = current_day - born_day
    days_alive = diff_y*365 + diff_m*30 + diff_d
    return days_alive

def hours_live(days_lived):
    hours_alive = days_lived*24
    return hours_alive

y_born = int(input("Year born: "))
m_born = int(input("Motn born: "))
d_born = int(input("Day born:  "))

days_lived = days_live(y_born,m_born,d_born)

print("The person has been living for ", days_lived , " days.")

hours_lived = hours_live(days_lived)

print("The person has been living for ", hours_lived ," hours.")
