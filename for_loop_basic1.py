#Basics
for x in range (0, 151):
    print(x)

#Multiples of 5
for x in range (5, 1005, 5):
    print(x)

#Counting, the Dojo Way
for x in range (1, 101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)