"""age = int(30)
height = float(1.80)
complx_num = complex(1 + 1j)

print(age , height , complx_num)"""

# Trianlge Area Calulator (TAC)

"""order = 1
if order == 1:
    order = input("Do you want to calculate the area of a triangle (a), or the perimeter (p) ? You can also exit (e), but why would you do that? ")
    if order == "a":
        base = int(input("Enter triangle-kun's base: "))
        height = int(input("Enter triangle-kun's height: "))
        TAC = str(0.5 * base * height)
        print("Calculating trangle-kun's area. . . Gamabre, triangle-kun!")
        print("Triangle-kun area is: " + TAC)        
    elif order == "p":
        side_a = int(input("Enter triangle kun's side A:"))
        side_b = int(input("Enter triangle kun's side B:"))
        side_c = int(input("Enter triangle kun's side C:"))
        perimeter = side_a + side_b + side_c
        print("Triangle-kun's pereimeter is " + str(perimeter))
    elif order == "e":
        exit
order = 1"""

# Rectanglus
"""rect_width = int(input("Enter rectangle width: "))
rect_length = int(input("Enter rectangle length: "))
rect_area = rect_width * rect_length
rect_perimeter = (rect_length + rect_width) * 2
print("Rectangle area = " + str(rect_area) + "\nRectangle perimeter: " + str(rect_perimeter))
"""

#Circlus radius

"""radius = int(input("Enter circle's radius "))
area = 3.14 * radius * radius
circ = 2 * 3.14 * radius
print("Area = " + str(area) + "\nCircunference = " + str(circ))"""

#Calculate the slope, x-intercept and y-intercept of y = 2x -2

"""slope = 2
y_intercept = -2
# m = y_intercept / x_intercept
x_intercept = slope * y_intercept

print("Slope = " + str(slope) + "\nY intercept = " + str(y_intercept) + "\nX intercept = " + str(x_intercept) )"""

#Calculate the value of y (y = x^2 + 6*x + 9). Try to use different x values and figure out at what x value y is going to be 0.
y = 0
x = 0//2 - 0/6 - 9
print(x)
y = x**2 + 6*x + 9
print(y)

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.

print(len("python"))
print(len("dragon"))
print(len("python") < len("dragon"))

# Use "and" operator to check if 'on' is found in both 'python' and 'dragon'

if "on" in "pyton" and "dragon":
    print("There's on in dragon")

# Use and operator to check if 'on' is found in both 'python' and 'dragon'

sentence = "I hope this course is not full of jargon. "
print("jargon" in sentence)

#Find the length of the text python and convert the value to float and convert it to string

text = "python"
text_length = float(len(text))
print("The word provided contains " + str(text_length) + " characters")

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

print(7 // 3 == int(2.7))

# Check if type of '10' is equal to type of 10
# Check if int('9.8') is equal to 10

print(type("10") == type(10))
print(int(9.8) == 10)

#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours = int(input("Enter weekly hours: "))
hour_rate = int(input("Enter the rate per hour: "))
weekly_earn = hours * hour_rate
print("Your income is " + str(weekly_earn) + " moneys per week") 

print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")