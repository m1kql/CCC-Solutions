# author: Mike Liang
# date: 01/27/2022

n = int(input())

antonia = 100
david = 100

for i in range(n):
    line = str(input())
    temp = line.split(" ")
    roll_antonia = int(temp[0])
    roll_david = int(temp[1])
    if roll_antonia > roll_david:
        david -= roll_antonia
    elif roll_antonia < roll_david:
        antonia -= roll_david
    elif roll_david == roll_antonia:
        pass

print(antonia)
print(david)
