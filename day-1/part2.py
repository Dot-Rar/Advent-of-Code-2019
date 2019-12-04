import math
inputs = []
fuel = 0

with open('input.txt', mode='r') as f:
    inputs = list(map(lambda s: int(s.strip()), f.readlines()))

def calculateFuel(i):
    return math.floor(i / 3) - 2

for i in inputs:
    f = calculateFuel(i)
    while f > 0:
        fuel += f
        f = calculateFuel(f)

print(fuel)
