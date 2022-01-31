# author: Mike Liang
# date: 01/27/2022

n = str(input())

if all(i in ("I", "O", "S", "H", "Z", "X", "N") for i in n):
    print("YES")
else:
    print("NO")
