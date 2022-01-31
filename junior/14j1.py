# author: Mike Liang
# date: 01/26/2022

a = int(input())
b = int(input())
c = int(input())

if a + b + c != 180:
    print("Error")
elif a == b == c == 60:
    print("Equilateral")
elif a != b and b != c and a != c:
    print("Scalene")
else:
    print("Isosceles")
