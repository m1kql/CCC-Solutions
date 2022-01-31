# author: Mike Liang
# date: 01/27/2022

m = int(input())
n = int(input())

mlist = []
nlist = []

ways = 0

for i in range(m):
    mlist.append(i + 1)

for i in range(n):
    nlist.append(i + 1)

for i in range(len(mlist)):
    if mlist[i] == 1 and 9 in nlist:
        ways += 1
    if mlist[i] == 2 and 8 in nlist:
        ways += 1
    if mlist[i] == 3 and 7 in nlist:
        ways += 1
    if mlist[i] == 4 and 6 in nlist:
        ways += 1
    if mlist[i] == 5 and 5 in nlist:
        ways += 1
    if mlist[i] == 6 and 4 in nlist:
        ways += 1
    if mlist[i] == 7 and 3 in nlist:
        ways += 1
    if mlist[i] == 8 and 2 in nlist:
        ways += 1
    if mlist[i] == 9 and 1 in nlist:
        ways += 1

if ways == 1:
    print(f"There is {ways} way to get the sum 10.")
else:
    print(f"There are {ways} ways to get the sum 10.")
