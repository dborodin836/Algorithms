from BubleSort import *
from InsertionSort import *
from SelectionSort import *
from CountSort import *
from MergeSort import *
from ShakerSort import *

if __name__ == '__main__':
    for func in [bubble, count, insertion, selection, count_dict, shaker]:
        lst = [5, 1, 0, 122, 12, -100, 200]
        func(lst)
        assert lst == [-100, 0, 1, 5, 12, 122, 200]

    assert merge([-1, 2, 3, 12, 12, 14, 99],
                 [-20, -15, -1, 0, 0, 14, 15, 17, 123]) == [-20, -15, -1, -1, 0, 0, 2, 3,
                                                            12, 12, 14, 14, 15, 17, 99, 123]
