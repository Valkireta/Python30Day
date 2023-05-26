#Here we have a person dictionary. Feel free to modify it!

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'gender' : "boy",
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }


#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

first_middle = int(len(person['skills'])/2) - 1
second_middle = int(len(person['skills'])/2)

if "skills" in person:
    if len(person["skills"]) % 2 == 0:
        print(person['skills'][first_middle])
        print(person['skills'][second_middle])
    else:
        print(person['skills'][second_middle])

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

if "skills" in person:
    if "Python" in person["skills"]:
        print("This person has Python in the Skills list")
    else:
        print("This person has no Python knowledge adquired")

#  * If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') - for more accurate results more conditions can be nested!

if 'skills' in person:
    if "JavaScript" and "React" in person['skills']:
        print('He is a front end developer')
    elif "Node" and "Python" and "MongoDB" in person['skills']: 
        print('He is a backend developer')
    elif "React" and "Node" and "MongoDB" in person['skills']:
        print('He is a fullstack developer')
    else: 
        print('unknown title') 
    

#  * If the person is married and if he lives in Finland, print the information in the following format:

full_name = person['first_name'] + " " + person['last_name']

if person['is_marred'] == True and person['country'] == 'Finland':
    if person['gender'] == "boy":
        print(full_name + " lives in Finland. He is married.")
    elif person['gender'] == "girl":
        print(full_name + " lives in Finland. She is married.")

elif person['is_marred'] == False and person['country'] == 'Finland':
    if person['gender'] == "boy":
        print(full_name + " lives in Finland, but he is not married :(")
    elif person['gender'] == "girl":
        print(full_name + " lives in Finland, but she is not married :(")

elif person['is_marred'] == True and person['country'] != 'Finland':
    if person['gender'] == "boy":
        print(full_name + " does not lives in Finland, but at least he is married :)")
    elif person['gender'] == "girl":
        print(full_name + "does not live in Finland, but at least she is married :)")
else:
    if person['gender'] == "boy":
        print("Hello" + full_name + ", it seems you're not married. Maybe you should travel to Findland and, who knows? You might find your other half ;)")
    elif person['gender'] == "girl":
        print("Hello" + full_name + ", it seems you're not married. Maybe you should travel to Findland and, who knows? You might find your other half ;)")