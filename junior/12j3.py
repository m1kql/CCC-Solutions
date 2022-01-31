# author: Mike Liang
# date: 01/27/2022

n = int(input())

star = "*"
x = "x"
space = " "

row1 = star * n + x * n + star * n
row2 = space * n + x * n + x * n
row3 = star * n + space * n + star * n

for i in range(n):
    print(row1)
for i in range(n):
    print(row2)
for i in range(n):
    print(row3)
