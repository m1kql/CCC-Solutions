# author: Mike Liang
# date: 01/31/2022

cities = []
a = input()

b = a.split(" ")

for i in b:
    cities.append(int(i))


dist_psa = [0] + cities

for i in range(1, len(cities) + 1):
    dist_psa[i] += dist_psa[i - 1]

for i in range(len(cities) + 1):
    for j in range(len(cities) + 1):
        dist = dist_psa[j] - dist_psa[i]
        print(abs(dist), end=" ")
    print("")

# distances = [sum(cities[: i + 1]) for i in range(len(cities))]
