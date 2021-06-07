from Bio.Seq import *
import numpy as np
import pandas as pd


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
    my_seq = Seq("AGTACACTGGT")
    print(my_seq)
    series = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(series)
