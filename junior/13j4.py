# author: Mike Liang
# date: 01/30/2022

t = int(input())  # allotted minutes
c = int(input())  # amount of chores

min_for_each_chore = []

while c > 0:
    min_for_each_chore.append(int(input()))
    c -= 1

min_for_each_chore.sort()

amnt_time_curr = 0
amnt_chores_possible = 0

for time in min_for_each_chore:
    amnt_time_curr += time
    if amnt_time_curr > t:
        break
    amnt_chores_possible += 1

print(amnt_chores_possible)
