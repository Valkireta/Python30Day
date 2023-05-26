# Day 2: 30 Days of python programming
# EXERCISE 1 

first_name = "Omar"
last_name = "Carcelen"
full_name = first_name + " " + last_name
country = "Spain"
city = "Barcelona"
age = 30
year = 2023
is_married = True
is_true = True
is_light_on = True

print("Hello " + full_name + ". " + "I've been waiting for you over " + str(age) + " years, but this day in " + str(year) + " you've finally come to " + city + ", " + country + ". ")

# EXERCISE 2
print(type(first_name), type(last_name))

print(len(first_name), len(last_name))
print(len(first_name) == len(last_name))

num_one = 5
num_two = 4
total = str(num_one + num_two)
diff = str(num_one - num_two)
product = str(num_one * num_two)
division = str(num_two / num_one)
reminder = str(num_one % num_two)
exp = str(num_one ** num_two)
floor_division = str(num_one // num_two)

print("You entered numbers " + str(num_one) + " and " + str(num_two) + ", so these are your results: " )
print("Total = " + total + "\nDiff = " + diff + "\nProduct = " + product + "\nDivision = " + division + "\nReminder = " + reminder + "\nExponential = " + exp + "\nFloor division = " + floor_division)

# Circle area calculator
import math

circle_radius = int(input("Enter the radius of your circle: "))
circle_area = float(math.pi * pow(circle_radius, 2))
circle_circum = float(2 * math.pi * circle_radius)

print("Your circle is as follows:\nRadius: " + str(circle_radius) + "\nArea: " + str(circle_area) + "\nCircum: " + str(circle_circum) )
