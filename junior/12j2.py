# author: Mike Liang
# date: 01/27/2022

depth = []

for i in range(4):
    depth.append(int(input()))

if depth[0] == depth[1] == depth[2] == depth[3]:
    print("Fish At Constant Depth")
elif depth[0] > depth[1] and depth[1] > depth[2] and depth[2] > depth[3]:
    print("Fish Diving")
elif depth[0] < depth[1] and depth[1] < depth[2] and depth[2] < depth[3]:
    print("Fish Rising")
else:
    print("No Fish")
