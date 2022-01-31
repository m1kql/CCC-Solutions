# author: Mike Liang
# date: 01/27/2022

y = int(input())
m = int(input())

old = 0

if y != m:
    diff = m - y
    old = diff + m
else:
    old = m

print(old)
