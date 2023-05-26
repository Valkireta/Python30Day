#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

driver_age = (input("Enter your age: "))

if int(driver_age) >= 18:
    print("You are old enough to learn to drive.")
elif int(driver_age) < 18:
    print("You need to wait " +  str(18 - int(driver_age)) + " more years to drive.")

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
#You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. 

my_age = 30
your_age = int(input("Enter your age: "))

if your_age < my_age:
  if your_age == my_age - 1:
    print("Oh, looks like you're " + str(my_age - your_age) + " year younger than me. Look at your, you're a baby!")
  else:
    print("Oh, looks like you're " + str(my_age - your_age) + " years older than me. Look at your, you're a baby!")

elif your_age > my_age:
  if your_age == my_age + 1:
    print("Really? You're " + str(your_age - my_age) + " year older than me? You're so old, old man!")
  else:
    print("Really? You're " + str(your_age - my_age) + " year older than me? You're so old, old man!")

elif my_age == your_age:
  print("Looks like we're the same age, but still I'm a way better than you. Sorry!")

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.

num1 = int(input("Enter the number: "))
num2 = int(input("Enter the other number: "))

if num1 > num2:
    print(str(num1) + " is smaller than " + str(num2) + " .... i think, but I might be wrong.\nCan we try some numbers other than " + str(num1) + " and " + str(num2) + " ?")
elif num1 < num2:
    print("I have no idea about numbers, so I will say that " + str(num1) + " is bigger than " + str(num2) + ", but why would you trust me.")
else:
    print(str(num1) + " looks similar to " + str(num2) + ". What kind of trickery be this?")


# Write a code which gives grade to students according to theirs scores:

score = int(input("Que nota has sacado en el examen? Introduce un valor (0-100): "))

if score > 0:
  if score >= 80:
      print("Tu grado es 'A', como en 'ASOMBROSO!' ")
  elif score > 70:
      print("Tu grado es 'B', muy BIEN, sigue así!")
  elif score > 60:
      print("Tu grado es 'C', CUIDADO, te acercas a zona peligrosa!")
  elif score > 50 :
      print("Tu grado es 'D', aprobado por los pelos. Si tienes DIFICULTADES, habla conmigo!")
  elif score >= 49:
      print("Tu grado es 'F', es decir suspendido. No te lo tomes como un FRACASO y esfuerzate mas, se que puedes hacerlo!")
else:
    print("Valor invalido")


# Check if the season is Autumn, Winter, Spring or Summer.  

month = (input("En que mes estamos? "))

if month == "Septiembre" or month == "Octubre" or month == "Noviembre":
  print("Oh, ya veo. Si estamos en " + str(month) + " quiere decir que estamos en Otoño.")
elif month == "Diciembre" or month == "Enero" or month == "Febrero":
  print("Ya estamos en " + str(month) + "? No me extraña que haga frio, estamos en Invierno.") 
elif month == month == "Marzo" or month == "Abril" or month == "Mayo":
  print("Ah, la Primavera. Me encanta esta estacion, en especial durante el mes de " + str(month))
elif month == "Junio" or month == "Julio" or month == "Agosto":
  print("No hace falta que me digas que es " + str(month) + ", de verdad. Con este calor se nota que es Verano")
else:
  print(str(month) + "? Eso es un mes?")

#The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("Enter a fruit: ")
if fruit in fruits:
    print("The fruit is already on the list, as you can see:")
    print(fruits)
else:
    fruits.append(fruit)
    print("We added " + fruit + " (whatever thatis) to the list of fruits. Uploading new list... :")
    print(fruits)

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

