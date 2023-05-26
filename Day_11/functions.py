import math
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers():
    num1 = 2
    num2 = 3
    total = num1 + num2
    return total
print("The sum of your numbers is :", add_two_numbers())

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def area_of_circle(rad):
    pi = math.pi
    area = pi * rad * rad
    result = 'The area of this circle = ' + str(round(area,2))
    return result
print(area_of_circle(10))


# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*nums):
    total = 0
    if all(isinstance(num, int) for num in nums): 
        for num in nums:
            total += num
        return total
    return "All values must be integers."
 

print(add_all_nums(1,5,5))


# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(c):
    total = (c * 9/5) +32
    return 'Converting {}°C will result in {}°F'.format(c, total)

print(convert_celsius_to_fahrenheit(76))    

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
        if month.lower() == ("march" or "april" or "may"):
            season = "It is Spring, season for flowers and bees!"
            return season
        elif month.lower() == ("june" or "july" or "august"):
            season = "It's Summertime and you know what that means.\nGonna head down to the beach and do some beachy things.\nIt's Summertime, it feels just right.\nGonna gather all my friends and we'll party through the night.\nIt's Summertime luh-uh-loving.\nIt's loving in the Summertime. (It's Summertime!)\nIt's Summertime luh-uh-loving.\nMy baby, why can't you be mine?"
            return season
        elif month.lower() == ("september" or "october" or "november"):
            season = "It's autumn, kinda boring to be honest."
            return season
        elif month.lower() == ("december" or "january" or "february"):
            season = "It's Winter! Cold weather means blanket + a movie, but not on Netflix anymore, those bastards increased the prize and limited the users."
            return season   
        return "Invalid input, let's try again"
        
    

print(check_season("march"))

# Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1, x2, y1, y2):
    slope = (y2 - y1) / (x2 - x1)
    return round(slope, 2)

print(calculate_slope(-1 ,0 ,0 ,-3))

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

def  solve_quadratic_eqn(a, b, c):
    pos_root = (-(b) + (b **2 - 4 * a * c)**0.5) / 2 * a
    neg_root = (-(b) - (b **2 - 4 * a * c)**0.5) / 2 * a
    return "The roots for the quadratic equation are {} and {}".format(pos_root, neg_root)

print(solve_quadratic_eqn(1, -3, -4))

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(lst):
    return [print(item) for item in lst]
    

print_list([1, 2, 7,31,674,235,37,154,583,3457,214365])

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(lst):
    new_lst = []
    for item in lst:
        new_lst.append(item)
    new_lst.reverse()
    return new_lst

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(lst):
    new_lst=[]
    for item in lst:
        new_lst.append(item.title())
    return new_lst

print(capitalize_list_items(["eyes","nose","hair","neck"]))

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

def add_item(list, item):
    list.append(item)
    return list

#The def above will add the items to the original list, while the one below will create a new list so it won't modify the original

def add_item(list, item):
    new_list = []
    for i in list:
        new_list.append(i)
    new_list.append(item)
    return new_list


food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      #[2, 3, 7, 9, 5]

print(food_stuff)
print(numbers)

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

def remove_item(list, item):
    list.remove(item)
    return list

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

#Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

def sum_of_numbers(num):
    total = 0
    for n in range(num +1):
        total += n
    return total



print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050


#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(num):
    total = 0
    for n in range(num +1):
        if n % 2 != 0:
            total += n
    return total

print(sum_of_odds(5))
print(sum_of_odds(10))
print(sum_of_odds(100))


#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_even(num):
    total = 0
    for n in range(num +1):
        if n % 2 == 0:
            total += n
    return total

print(sum_of_even(5))
print(sum_of_even(10))
print(sum_of_even(100))


#Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.


def evens_and_odds(num):
    evens = 0
    odds = 0
    for n in range(num +1):
        if n % 2 == 0:
            evens += 1
        elif n % 2 != 0:
            odds += 1
    return "The number of odds is {}.\nThe number of evens is {}.".format(evens,odds)
     



print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.



#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(num):
    total = 1
    for n in range(1, num + 1):
        total *= n
    return total

print(factorial(5))

#Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(item):
    if len(item) == 0:
        return "It is empty"
    else:
        return "It is not empty"
    
print(is_empty(["Empty list"]))

#Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

number_list = [99,86,87,87,88,111,86,103,87,94,78,77,85,86]

def calculate_mean(lst):
    total = 0
    for item in lst:
        total += item
    mean = total / len(lst)
    return "The mean value of the list provided is {:.2f}.".format(mean)

print(calculate_mean(number_list))

def calculate_median(lst):
    median = 0
    lst.sort()
    middle = int(len(lst)/2)
    if len(lst) % 2 != 0:
        median = lst[middle]
        return "The median value of the list provided is {}.".format(median)
    elif len(lst) %2 == 0:
        median = lst[middle] + lst[middle-1] / 2
        return "The median value of the list provided is {:.2f}.".format(median)
    
print(calculate_median(number_list))

        
        
def calculate_mode(lst):
    count = 0
    for item in lst:
        current_count = lst.count(item)
        if current_count > count:
            count = current_count
            mode = item
    
    return "The mode value of the list provided is {}.".format(mode)

print(calculate_mode(number_list))


def calculate_range(lst):
    lst.sort()
    rnge = lst[-1] - lst[0]
    return "The range value of the list provided is {}.".format(rnge)

print(calculate_range(number_list))


def calculate_variance(lst):
    total = 0
    sq_sum = 0
    for item in lst:
        total += item
    mean = total / len(lst)
    for item in lst:
        sq_sum += ((item - mean)**2)
    variance = sq_sum / (len(lst) -1)
    return "The variance value of the list provided is {:.1f}.".format(variance)


print(calculate_variance([46,69,32,60,52,41]))
    


def calculate_std(lst):
    total = 0
    sq_sum = 0
    for item in lst:
        total += item
    mean = total / len(lst)
    for item in lst:
        sq_sum += ((item - mean)**2)
    variance = sq_sum / (len(lst) -1)
    std = variance ** 0.5
    return "The standard deviation from the mean for each value is {:.2f}.".format(std)


print(calculate_std([46,69,32,60,52,41]))


# Write a function called is_prime, which checks if a number is prime.

def is_prime(n):
    is_it = False
    if n == 1 :
        return "Nº {} is not prime".format(n)
    elif n > 1 :
        for i in range(2,n):
            if (n % i) == 0:
                is_it = True
    if is_it == True:
        return "Nº {} is prime".format(n)
    else:
        return "Nº {} is not prime".format(n)
                        


print(is_prime(8))  

# Write a functions which checks if all items are unique in the list.

def are_unique(lst):
    unique = True
    for item in lst:
        if lst.count(item) > 1:
            unique = False
    if unique == True:
        return "All items are unique"
    else:
        return "List contain duplicates"

print(are_unique([1,2,3,4,5,6,7]))

# Write a function which checks if all the items of the list are of the same data type.

def are_same_type(lst):
    same = True
    for item in lst:
        if type(item) != type(lst[0]):
            same = False
            break          
        elif type(item) == type(lst[0]):
            continue
    if same == False:
        return "List contain different data types."
    elif same == True:
        return "All data types are the same."

print(are_same_type([True,2,3,4,5,False]))


# Write a function which check if provided variable is a valid python variable

def id_check(id):
    valid = True
    if id.isidentifier() == False:
        valid = False
    if valid == True:
        return "This is a valid Python variable"
    elif valid == False:
        return "This is not a valid Python variable"

print(id_check("1variable1"))

# Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
