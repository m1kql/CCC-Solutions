# author: Mike Liang
# date: 01/28/2022

n = int(input())
m = int(input())

adj = []
nouns = []

for i in range(n):
    adj.append(str(input()))

for i in range(m):
    nouns.append(str(input()))

similes = []

for i in range(len(adj)):
    for noun in nouns:
        similes.append(str(adj[i] + " as " + noun))

for i in similes:
    print(i)
