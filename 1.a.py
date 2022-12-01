#!/usr/bin/env python3

data = open("inputs/1.txt", "r")

currentMax = 0
culm = 0

for line in data:
    if line == "\n":
        if culm > currentMax:
            currentMax = culm
        culm = 0
    else:
        culm = culm + int(line)

print(currentMax)

