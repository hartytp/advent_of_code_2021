import numpy as np


with open('data.txt') as file:
    data = np.array(file.readlines(), dtype=int)
increased = sum(np.diff(data) > 0)
print(increased)
