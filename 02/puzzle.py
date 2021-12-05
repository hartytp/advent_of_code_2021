import numpy as np


with open('data.txt') as file:
    data = file.read().splitlines()
# data = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']

data = ';'.join(data)
part_I = (data.replace('forward', 'position +=')
              .replace('down', 'depth +=')
              .replace('up', 'depth -='))

depth = 0
position = 0
exec(part_I)
print(f"Day 2: position {position}, depth {depth}, product {position*depth}")

state = np.array([0, 0, 0])  # aim, pos, depth
part_II = (data.replace('forward', 'state += np.array([0, 1, state[0]]) * ')
               .replace('down', 'state[0] +=')
               .replace('up', 'state[0] -='))
exec(part_II)
print(f"Day 2: position {state[1]}, depth {state[2]}, "
      f"product {np.prod(state[1:])}")
