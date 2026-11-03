#write a function(program) to convert celcius to fahrenheit and fahrenheit to celcius.
# F=C*(9/5)+32
#also identify the temp that is same in C (Celcius) and F (Fahrenheit) and print it.

#Function to convert C -> F
def celsius_to_fahrenheit(C):
    F = C * (9/5) + 32
    return F

#Function to convert F -> C
def fahrenheit_to_celsius(F):
    C = (F - 32) * (5/9)
    return C

#convery temperatures
C = float(input("Enter temperature in Celsius:"))
print("Fahrenheit =", celsius_to_fahrenheit(C))

F = float(input("Enter temperature in Fahrenheit:"))
print("Celsius =", fahrenheit_to_celsius(F))

#temp that is same in celcius and fahrenheit
for temp in range(-100,101):
    if celsius_to_fahrenheit(temp) == temp:
        print ("Same temperature in Celsius and Fahrenheit:",temp)


