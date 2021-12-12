from BubleSort import *
from InsertionSort import *
from SelectionSort import *
from CountSort import *

if __name__ == '__main__':
    assert bubble([5, 1, 0, 122, 12, -100, 200]) == [-100, 0, 1, 5, 12, 122, 200]
    a = [5, 1, 0, 122, 12, -100, 200]
    bubble_sorted(a)
    assert a == [-100, 0, 1, 5, 12, 122, 200]
    assert selection([5, 1, 0, 122, 12, -100, 200]) == [-100, 0, 1, 5, 12, 122, 200]
    a = [5, 1, 0, 122, 12, -100, 200]
    selection_sorted(a)
    assert a == [-100, 0, 1, 5, 12, 122, 200]
    assert insertion([5, 1, 0, 122, 12, -100, 200]) == [-100, 0, 1, 5, 12, 122, 200]
    a = [5, 1, 0, 122, 12, -100, 200]
    insertion_sorted(a)
    assert a == [-100, 0, 1, 5, 12, 122, 200]
    assert count([5, 1, 0, 122, 12, -100, 200]) == [-100, 0, 1, 5, 12, 122, 200]
    a = [5, 1, 0, 122, 12, -100, 200]
    count_sorted(a)
    assert a == [-100, 0, 1, 5, 12, 122, 200]