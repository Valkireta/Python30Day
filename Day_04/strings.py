# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

word1 = "Thirty"
word2 = "Days"
word3 = "Of"
word4 = "Python"
space = " "
sentence = word1 + space + word2 + space + word3 + space + word4
print(sentence)

word1 = "Coding"
word2 = "For"
word3 = "All"
sentence = word1 + space + word2 + space + word3
print(sentence)

#Declare a variable named company and assign it to an initial value "Coding For All".

company = "Coding For All"

#Print the variable company using print().

print(company)

#Print the length of the company string using len() method and print().

print(len(company))

#Change all the characters to uppercase letters using upper() method.

print(company.upper())

#Change all the characters to lowercase letters using lower() method.

print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize())
print(company.title())
print(company.swapcase())


#Cut(slice) out the first word of Coding For All string.

first_word = company[0:7]
print(first_word)

#Check if Coding For All string contains a word Coding using the method index, find or other methods.

print(company.index("Coding"), company.rindex("Coding"))

#Replace the word coding in the string 'Coding For All' to Python.

company = company.replace("Coding", "Python")
print(company)

#Change Python for Everyone to Python for All using the replace method or other methods.

company = company.replace("All", "Everyone")
print(company)

#Split the string 'Coding For All' using space as the separator (split()) .

print(company.split(" "))

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", "))


#What is the character at index 0 in the string Coding For All.

sentence = "Coding for all"
first_letter = sentence[0]
print(first_letter)


#What is the last index of the string Coding For All.

last_index = len(sentence) -1
last_letter = sentence[last_index]
print(last_letter)


#What character is at index 10 in "Coding For All" string.

print(sentence[10])

#Create an acronym or an abbreviation for the name 'Python For Everyone'.

PFE = "Python For Everyone"

#Create an acronym or an abbreviation for the name 'Coding For All'.

CFA = "Coding For All"

#Use index to determine the position of the first occurrence of C in Coding For All.

print(CFA.index("C"))

#Use index to determine the position of the first occurrence of F in Coding For All.

print(PFE.index("F"))

#Use rfind to determine the position of the last occurrence of l in Coding For All People.

print(CFA.rfind("l"))

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

b_cause = "You cannot end a sentence with because because because is a conjunction"
b_string = "because"
first_b = b_cause.find(b_string)
print(first_b)


#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

last_b = b_cause.rindex(b_string)
print(last_b)

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

slce_out = b_cause[31:54]
print(slce_out)

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.

string = '   Coding For All      '
star_string = string.index("C")
end_string = string.rindex("l") + 1

print(string[star_string:end_string])

#Which one of the following variables return True when we use the method isidentifier():
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" / ".join(libraries))

# Use the new line escape sequence to separate the following sentences.
print("I am enjoying this challenge.\nI just wonder what is next.")

# Use a tab escape sequence to write the following lines.
print("Name\t   Age \t Country \t City \nAsabeneh   250 \t Finland \t Helsinki")

# Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, area))

# Make the following using string formatting methods:
num1 = 8
num2 = 6
print("{} + {} = {}".format(num1, num2, num1 + num2))
print("{} + {} = {}".format(num1, num2, num1 - num2))
print("{} + {} = {}".format(num1, num2, num1 * num2))
print("{} + {} = {:.2f}".format(num1, num2, num1 / num2)) # {:.2f} Limit to 2 digits
print("{} + {} = {}".format(num1, num2, num1 ** num2))
print("{} + {} = {}".format(num1, num2, num1 // num2))
