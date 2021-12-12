import numpy as np

GRID_SIZE = 5
lines = []
size = [0, 0]

with open('data.txt') as file:
    for line in file:
        start, stop = line.split('->')
        lines.append((np.array(start.split(','), dtype=int),
                     (np.array(stop.split(','), dtype=int))))
        size = [max([size[idx], lines[-1][0][idx] + 1, lines[-1][1][idx] + 1])
                for idx in range(2)]

straight_lines = []
for start, stop in lines:
    if any(start == stop):
        straight_lines.append((start, stop))

vents = np.zeros(size)
for start, stop in straight_lines:
    if start[0] == stop[0]:
        sgn = 1 if stop[1] > start[1] else -1
        vents[start[0], start[1]:(stop[1] + sgn):sgn] += 1
    else:
        sgn = 1 if stop[0] > start[0] else -1
        vents[start[0]:(stop[0] + sgn):sgn, start[1]] += 1

print(f"Day 4 part I: danger points {np.sum(vents>=2)}")
# print(f"Day 3 part I: loosing grid {winning_grids[-1]}, "
#       f"score {scores[-1]}")
