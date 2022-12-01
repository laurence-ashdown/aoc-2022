#!/usr/bin/env python3

from heapq import heappush, nlargest

data = open("inputs/1.txt", "r")

culm = 0

heap = []

for line in data:
    if line == "\n":
        heappush(heap, culm)
        culm = 0
    else:
        culm = culm + int(line)

print(sum(nlargest(3, heap)))


