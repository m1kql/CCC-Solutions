# author: Mike Liang
# date: 01/31/2022

n = int(input())

resp = []

c = 0

for i in range(n):
    resp.append(input())


for i in range(n):
    if input() == resp[i]:
        c += 1

print(c)
