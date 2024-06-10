"""
Makes the input for the exercise. Don't look at this
until you're done!
"""


import sys
import numpy as np

try:
    input_size = int(sys.argv[1])
    input_offset = int(0.1 * input_size)
    input_size += input_offset
except:
    print("Please input the size of the output you would like.")
    exit(1)

for input in range(2):
    values = np.random.rand(input_size)
    ids = np.arange(input_size)
    np.random.shuffle(ids)

    np.savetxt(
        f"input_{input}.txt",
        np.c_[values[:-input_offset], ids[:-input_offset]],
        fmt=["%5e", "%d"],
    )
