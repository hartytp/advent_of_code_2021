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

winning_grids = []
winning_draws = []
for draw in draws:
    for idx in range(len(grids)):
        if idx in winning_grids:
            continue
        hits[idx] = np.logical_or(hits[idx], grids[idx] == draw)

    # See if we have a winner
    for idx in range(len(grids)):
        if idx in winning_grids:
            continue
        col_hits = np.sum(hits[idx], axis=0)
        row_hits = np.sum(hits[idx], axis=1)
        if GRID_SIZE in col_hits or GRID_SIZE in row_hits:
            winning_grids.append(idx)
            winning_draws.append(draw)

scores = np.zeros(len(grids), dtype=int)
for idx in range(len(grids)):
    winning_draw = winning_draws[idx]
    winning_grid = winning_grids[idx]
    misses = np.logical_not(hits[winning_grid])
    score = winning_draw * np.sum(misses * grids[winning_grid])
    scores[idx] = score

print(f"Day 3 part I: winning grid {winning_grids[0]}, "
      f"score {scores[0]}")
print(f"Day 3 part I: loosing grid {winning_grids[-1]}, "
      f"score {scores[-1]}")
