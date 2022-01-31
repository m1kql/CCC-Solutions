# author: Mike Liang
# date: 01/28/2022

burger = int(input())
sides = int(input())
drink = int(input())
dessert = int(input())

cal = 0

if burger == 4:
    cal += 0
elif burger == 1:
    cal += 461
elif burger == 2:
    cal += 431
elif burger == 3:
    cal += 420

if drink == 4:
    cal += 0
elif drink == 1:
    cal += 130
elif drink == 2:
    cal += 160
elif drink == 3:
    cal += 118

if sides == 4:
    cal += 0
elif sides == 1:
    cal += 100
elif sides == 2:
    cal += 57
elif sides == 3:
    cal += 70

if dessert == 4:
    cal += 0
elif dessert == 1:
    cal += 167
elif dessert == 2:
    cal += 266
elif dessert == 3:
    cal += 75

print(f"Your total Calorie count is {cal}.")
