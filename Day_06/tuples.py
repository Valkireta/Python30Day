# Create an empty tuple

le_tuple = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

bros = ("Oriol", "Dexter", "Casey", "Kava", "Sean")
sis = ("Kira", "Irina", "Yennefer")

print(bros)
print(sis)

# Join brothers and sisters tuples and assign it to siblings

siblings = bros + sis
print(siblings)

# How many siblings do you have?


print("I have a total of " + str(len(siblings)) + " wonderful siblings.")

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members

parents = ("Pedro", "Silvia")
family_members = siblings + parents
family_members
print (family_members)

# Unpack siblings and parents from family_members

first_sibling, second_sibling, third_sibling, fourth_sibling, fifth_sibling, sixth_sibling, seventh_sibling, eight_sibling, *parent = family_members
print(sixth_sibling)
print(parent)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ("Apple", "Banana", "Melon", "Tangerine")
vegetables = ("Onion", "Carrot", "Tomato", "Potato")
animal_products = ("Chicken", "Jamon", "Steak")

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
# Change the about food_stuff_tp tuple to a food_stuff_lt list

food_Stuff_lt = list(food_stuff_tp)
print(food_Stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

middle_item = int(len(food_stuff_tp) / 2)
print(food_stuff_tp[middle_item])


# Slice out the first three items and the last three items from food_staff_lt list

print(food_Stuff_lt[1:4] , food_Stuff_lt[-3:])

# Delete the food_staff_tp tuple completely

del(food_stuff_tp)


# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)