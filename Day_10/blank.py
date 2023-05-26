from countries import countries

# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

for country in countries:
    if "land" in country:
        print(country)

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruits = ['banana', 'orange', 'mango', 'lemon']

for fruit in reversed(fruits):
    print(fruit)

# Go to the data folder and use the countries_data.py file.

from countries_data import country_dicc


# What are the total number of languages in the data

languages = 0
for language in country_dicc:
    languages += 1
    print(languages)

# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world