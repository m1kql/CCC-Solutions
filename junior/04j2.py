# author: Mike Liang
# date: 01/28/2022

lb = int(input())
ub = int(input())

years = []

yearrange = ub - lb + 1

for i in range(yearrange):
    if i % 4 == 0 and i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
        years.append(i)

finalyears = []

for i in years:
    finalyears.append(lb + i)


for i in finalyears:
    print(f"All positions change in year {i}")
