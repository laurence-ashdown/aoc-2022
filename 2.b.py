#!/usr/bin/env python3

data = open('inputs/2.txt', 'r')

score_map = {
        'A': 1,
        'B': 2,
        'C': 3,
        }

win_map = {
        'A': 'B',
        'B': 'C',
        'C': 'A'
        }

loss_map = {
        'A': 'C',
        'B': 'A',
        'C': 'B'
        }


draw = 3
draw_char = 'Y'

win = 6
win_char = 'Z'

score = 0

for line in data:
    opponent = line[0]
    me = line[2]

    # win
    if me == win_char:
        score += win + score_map[win_map[opponent]]

    # draw
    elif me == draw_char:
        score += draw + score_map[opponent]

    else:
        score += score_map[loss_map[opponent]]

print(score)




