import numpy as np
import numpy.matlib

GRID_SIZE = 5
with open('data.txt') as file:
    header = file.readline()
    draws = np.array(header.split(','), dtype=int)

    grids = []
    hits = []
    while file.readline() == '\n':
        grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
        for idx in range(GRID_SIZE):
            line = file.readline()
            grid[idx, :] = np.array(line.split(), dtype=int)
        grids.append(grid)
        hits.append(np.zeros((GRID_SIZE, GRID_SIZE), dtype=bool))


for draw in draws:
    for idx in range(len(grids)):
        hits[idx] = np.logical_or(hits[idx], grids[idx] == draw)

    # See if we have a winner
    for idx in range(len(grids)):
        col_hits = np.sum(hits[idx], axis=0)
        row_hits = np.sum(hits[idx], axis=1)
        if GRID_SIZE in col_hits or GRID_SIZE in row_hits:
            winning_grid = idx
            break
    else:
        continue
    break

misses = np.logical_not(hits[winning_grid])
score = draw * np.sum(np.array(misses, dtype=int) * grids[winning_grid])

print(f"Day 3 part I: winning grid {winning_grid}, "
      f"score {score}")
