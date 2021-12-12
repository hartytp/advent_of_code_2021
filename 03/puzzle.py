import numpy as np
import numpy.matlib


with open('data.txt') as file:
    data = file.read().splitlines()

# data = np.array(['00100', '11110', '10110', '10111', '10101', '01111', '00111',
#                  '11100', '10000', '11001', '00010', '01010'])
bits = np.array([(list(line)) for line in data], dtype=int)


def rank_bits(bits):
    most = np.array(np.sum(bits, axis=0) >= (bits.shape[0]/2), dtype=int)
    least = np.array(np.sum(bits, axis=0) < (bits.shape[0]/2), dtype=int)
    return most, least


def bin_to_int(bin_num):
    return int(''.join([str(x) for x in bin_num]), 2)


gamma_bits, eps_bits = rank_bits(bits)
gamma = bin_to_int(gamma_bits)
eps = bin_to_int(eps_bits)
print(f"Day 3 part I: gamma {gamma}, eps {eps}, prod {gamma*eps}")


def rank_filtered(bits, rank_index):
    matches = np.array([True]*bits.shape[0])
    for bit_idx in range(bits.shape[1]):
        matched = bits[matches, :]
        matched_bit = rank_bits(matched)[rank_index][bit_idx]
        matches = np.logical_and(matches, bits[:, bit_idx] == matched_bit)

        if sum(matches) == 1:
            return bits[np.argwhere(matches), :].flatten()


oxy = bin_to_int(rank_filtered(bits, 0))
c02 = bin_to_int(rank_filtered(bits, 1))
print(f"Day 3 part I: oxygen {oxy}, CO2 {c02}, prod {oxy*c02}")
