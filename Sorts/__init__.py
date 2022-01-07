from BubleSort import *
from InsertionSort import *
from SelectionSort import *
from CountSort import *
from ShakerSort import *
from MergeSort import merge_sort

if __name__ == '__main__':
    for func in [bubble, count, insertion, selection, count_dict, shaker, merge_sort]:
        lst = [5, 1, 0, 122, 12, -100, 200]
        func(lst)
        assert lst == [-100, 0, 1, 5, 12, 122, 200]

