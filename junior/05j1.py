# author: Mike Liang
# date: 01/27/2022

daymin = int(input())
evemin = int(input())
weekendmin = int(input())

t = 0.25 * (daymin - 100)
p = 0.45 * (daymin - 250)


plan_a = (t if t > 0 else 0) + (0.15 * evemin) + (0.2 * weekendmin)
plan_b = (p if p > 0 else 0) + (0.35 * evemin) + (0.25 * weekendmin)

print(f"Plan A costs {str(round(plan_a, 2))}")

print(f"Plan B costs {str(round(plan_b, 2))}")

if round(plan_b, 2) == round(plan_a, 2):
    print("Plan A and B are the same price.")
elif round(plan_a, 2) > round(plan_b, 2):
    print("Plan B is cheapest.")
else:
    print("Plan A is cheapest.")
