# author: Mike Liang
# date: 01/31/2022

n = int(input())

t_and_T = 0
s_and_S = 0

line = ""

for i in range(n):
    line += input()

t = line.count("t")
T = line.count("T")
s = line.count("s")
S = line.count("S")
s_and_S += s + S
t_and_T += t + T

if s_and_S > t_and_T:
    print("French")
elif s_and_S < t_and_T:
    print("English")
else:
    print("French")
