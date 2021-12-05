import numpy as np


with open('data.txt') as file:
    data = np.array(file.readlines(), dtype=int)
# data = np.array([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])  # check data

# Part I
increased = sum(np.diff(data) > 0)
print(f"Part II: {increased} increased measurements")

# Part II
cumsum = np.cumsum(np.insert(data, 0, 0))
print(cumsum)
winsum = cumsum[3:] - cumsum[:-3]
increased = sum(np.diff(winsum) > 0)
print(f"Part II: {increased} increased averaged measurements")
