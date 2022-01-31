# author: Mike Liang
# date: 01/27/2022

k = int(input())
word = str(input())

decode = ""

for p in range(len(word)):
    shift = 3 * (p + 1) + k
    # print(shift)
    # get current ascii value
    ascii_num = ord(word[p])
    newchar = ascii_num - shift
    if newchar < ord("A"):
        newchar += 26
    decode += chr(newchar)

print(decode)
