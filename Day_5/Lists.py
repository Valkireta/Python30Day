# Declare an empty list

le_list = []


# Declare a list with more than 5 items

le_list = ["Rice", "Pasta", "Vegetables", "Ice-cream", "Chocolat"]

# Find the length of your list

print(len(le_list))

# Get the first item, the middle item and the last item of the list

print(le_list[0])
print(le_list[-1])
middle_item = int(len(le_list)/2)
print(le_list[middle_item])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ["Omar", 30, 1.80, "Single", "Of the street, House in the middle."]
print(mixed_data_types)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()

print(it_companies)

# Print the number of companies in the list

print("There's a total of " + str(len(it_companies)) + " companies on the list." )

# Print the first, middle and last company

print("The first company on the list is: " + it_companies[0])
middle_item_it = int(len(it_companies)/2) + 1
print("The company on the middle of the list is: " + it_companies[middle_item_it])
print("The last company on the list is: " + it_companies[-1])


# Print the list after modifying one of the companies

it_companies[4] = "Cisco"
print(it_companies)

# Add an IT company to it_companies

it_companies.append("Intel")
print(it_companies)


# Insert an IT company in the middle of the companies list

it_companies.insert(middle_item_it, "Dell")
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)

it_companies[4] = it_companies[4].upper()
print(it_companies)

# Join the it_companies with a string '#;  '

print('#;  '.join(it_companies))

# Check if a certain company exists in the it_companies list.

print("intel" in it_companies) # False

# Sort the list using sort() method

it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method

it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list

print(it_companies[3:])

# Slice out the last 3 companies from the list

print(it_companies[0:-3])

# Slice out the middle IT company or companies from the list

print(it_companies)
print(it_companies[0:middle_item_it] + it_companies[middle_item_it + 1:])

# Remove the first IT company from the list

it_companies.remove("Oracle")
print(it_companies)

# Remove the middle IT company or companies from the list

it_companies.pop(middle_item_it)
print(it_companies)

# Remove the last IT company from the list

it_companies.pop(-1)
print(it_companies)

# Remove all IT companies from the list

del it_companies[0:]
print(it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.

full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
full_stack.insert(5,"Python")
full_stack.insert(5,"SQL")
print(full_stack)

# The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age

ages.sort()
print(ages)
print("The min age on the list is " + str(min(ages)) + ", while the max age on the list is " + str(max(ages)))

# Add the min age and the max age again to the list

ages.append(max(ages))
ages.append(min(ages))
ages.sort()
print(ages)


# Find the median age (one middle item or two middle items divided by two)

age_median = (max(ages) + min(ages)) / 2
print("The median age of that list is: " + str(age_median))

# Find the average age (sum of all items divided by their number )

age_average = sum(ages) / len(ages)
print("The average age for the provided list is: " + str(age_average))

# Find the range of the ages (max minus min)

age_range = max(ages) - min(ages)
print("Tha range of ages is: " + str(age_range))


# Compare the value of (min - average) and (max - average), use abs() method

value1 = abs(min(ages) - age_average)
value2 = abs(max(ages) - age_average)
print(value1, value2)