#!/usr/bin/env python3

data = open('inputs/2.txt', 'r')

score_map = {
        'A': 1,
        'X': 1,
        'B': 2,
        'Y': 2,
        'C': 3,
        'Z': 3
        }

win_map = {
        'A': 'Y',
        'B': 'Z',
        'C': 'X'
        }

compliment_map = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
        }

draw = 3
win = 6
score = 0

for line in data:
    opponent = line[0]
    me = line[2]

    # always get move value
    score += score_map[me]

    # win
    if win_map[opponent] == me:
        score += win

    # draw
    if compliment_map[opponent] == me:
        score += draw

print(score)




