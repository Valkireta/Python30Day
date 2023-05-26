# Create an empty dictionary called dog

dog = {}

# Add name, color, breed, legs, age to the dog dictionary

dog = {"name":"Kira", "color":"brown","breed":"Cutie","legs":"4","age":"10"}
print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student = {"first_name":"Omar", "last_name":"Monioso", "gender":"Dude", "age":"30", "marital status":"Single", "skills":["Videogames", "Programming", "Cooking", "Guitar", "Logic", "Good in bed"], "country":"Spain", "city":"Cerdanyola", "address":"Fake street, 123"}

# Get the length of the student dictionary

print(len(student))

# Get the value of skills and check the data type, it should be a list

print(type(student["skills"]))

# Modify the skills values by adding one or two skills

student["skills"].append("Educated")
student["skills"].append("Exelent customer service")
print(student["skills"])

# Get the dictionary keys as a list

print(student.keys())

# Get the dictionary values as a list

print(student.values())

# Change the dictionary to a list of tuples using items() method

print(student.items())

# Delete one of the items in the dictionary

del student["marital status"]
print(student.keys())

# Delete one of the dictionaries

del dog