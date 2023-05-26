# Iterate 0 to 10 using for loop, do the same using while loop.

for n in range(11):
    print(n)
else:
    print("FOR count ended at ", n)

count = 0
while count !=11:
    print(count)
    count = count + 1
else:
    print("WHILE count ented when count reached ", count)

# Iterate 10 to 0 using for loop, do the same using while loop.

for n in range(10,0,-1):
    print(n)

count = 10
while count !=0:
    print(count)
    count = count - 1
else:
    print(count)

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:

for n in range (8):
    print( "#" * n)

triangle = 8

while triangle !=0:
    print("#" * triangle)
    triangle = triangle - 1

# Use nested loops to create the following:

size = 8
desize = 0

while size != 0:
    print("# " * size + "# " * desize) 
    size -= 1
    desize += 1


# Print the following pattern:

for n in range(11):
    print(n ," x ", n ," = ", n * n)

