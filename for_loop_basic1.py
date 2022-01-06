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

#Whoa. That Sucker's Huge
sum = 0
for x in range (1, 500001, 2):
    sum += x
print(sum)

#Countdown by Fours
for x in range (2018, 0, -4):
    print(x)

#Flexible Counter
low = 2
high = 9
mult = 3

for x in range (low, high + 1):
    if x % mult == 0:
        print(x)