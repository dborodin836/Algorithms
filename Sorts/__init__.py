from BubleSort import *
from InsertionSort import *
from SelectionSort import *
from CountSort import *

if __name__ == '__main__':
    for func in [bubble, bubble_sorted, count, count_sorted,
                 insertion, insertion_sorted, selection, selection_sorted]:

        if 'sorted' not in str(func):
            assert func([5, 1, 0, 122, 12, -100, 200]) == [-100, 0, 1, 5, 12, 122, 200]

        if 'sorted' in str(func):
            lst = [5, 1, 0, 122, 12, -100, 200]
            func(lst)
            assert lst == [-100, 0, 1, 5, 12, 122, 200]
