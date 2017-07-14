#!/usr/bin/env python

# Martin Kersner, m.kersner@gmail.com
# 2017/07/13

import numpy as np
from hailstone import *

def main():
    arr_len = 6
    start   = 10
    step    = 4
    end     = 50000

    sequences = []

    for idx in range(start, end, step):
        sequences.append(Hailstone(idx).generate_sequence()[:arr_len])

    np.save("hailstone_sequences_50000.npy", np.array(sequences))

if __name__ == "__main__":
    main()
