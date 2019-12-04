import math
inputs = []

with open('input.txt', mode='r') as f:
    inputs = list(map(lambda s: int(s.strip()), f.readlines()))

print(sum(map(lambda i: math.floor(i / 3) - 2, inputs)))
