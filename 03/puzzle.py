import numpy as np


with open('data.txt') as file:
    data = file.read().splitlines()

# data = ['00100', '11110', '10110', '10111', '10101', '01111', '00111',
#         '11100', '10000', '11001', '00010', '01010']
bits = np.array([(list(line)) for line in data], dtype=int)
num_bits = bits.shape[1]

gamma_bits = np.array(np.sum(bits, axis=0) > (bits.shape[0]/2), dtype=int)
gamma_bits = np.insert(gamma_bits, 0, np.zeros(8 - (num_bits % 8)))
gamma_bits = np.reshape(gamma_bits, (len(gamma_bits) // 8, 8))
gamma = np.packbits(gamma_bits)
gamma = np.sum(np.left_shift(gamma, np.arange(len(gamma))[::-1]*8),
               dtype=np.uint32)

mask = (1 << num_bits) - 1
eps = np.bitwise_and(np.invert(gamma), mask)
print(f"Day 3: gamma {gamma}, eps {eps}, prod {gamma*eps}")
