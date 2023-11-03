def c_f(c):
    return(c*9/5)+32

def f_c(f):
    return(f-32)*5/9

print("1. Convert Celsius to Fahrenheit")
print("2. Convert Fahrenheit to Celsius")
print("3. Quit")

x = input("Your choice: ")

if x == "1":
    c = float(input("Temperature in Celcius: "))
    f= c_f(c)
    print(f"{c} Celsius is {f} Fahrenhait")

elif x == "2":
    f =float(input("Temparature in Fahrenheit: "))
    c = f_c(f)
    print(f"{f} Fahrenhait is {c} Celcius")

elif x == "3":
    print("Goodbye!")

else:
    print("Invalid choice. Please enter 1, 2, or 3.")