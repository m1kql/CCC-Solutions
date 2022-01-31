# author: Mike Liang
# date: 01/27/2022

speedlim = int(input())
speed = int(input())

if speed <= speedlim:
    print("Congratulations, you are within the speed limit!")
elif speed >= speedlim + 31:
    print("You are speeding and your fine is $500.")
elif speed >= speedlim + 21 and speed <= speedlim + 30:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $100.")
