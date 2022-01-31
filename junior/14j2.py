# author: Mike Liang
# date: 01/26/2022

n = int(input())

votes = input()

a = 0
b = 0

for i in range(len(votes)):
    if votes[i] == "A":
        a += 1
    elif votes[i] == "B":
        b += 1

if a > b:
    print("A")
elif b > a:
    print("B")
else:
    print("Tie")
