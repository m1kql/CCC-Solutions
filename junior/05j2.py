# author: Mike Liang
# date: 01/27/2022

a = int(input())
b = int(input())

num_rsa = 0


for i in range(a, b + 1):
    divisor = 0
    for j in range(i + 1):
        if i % (j + 1) == 0:
            divisor += 1
    if divisor == 4:
        num_rsa += 1

print(f"The number of RSA numbers between {a} and {b} is {num_rsa}")
