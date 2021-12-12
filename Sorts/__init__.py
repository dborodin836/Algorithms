import BubleSort
import SelectionSort

if __name__ == '__main__':
    assert BubleSort.bubble([5, 1, 0, 122, 12, -100, 200]) == [-100, 0, 1, 5, 12, 122, 200]
    a = [5, 1, 0, 122, 12, -100, 200]
    BubleSort.bubble_sorted(a)
    assert a == [-100, 0, 1, 5, 12, 122, 200]
    assert SelectionSort.selection([5, 1, 0, 122, 12, -100, 200]) == [-100, 0, 1, 5, 12, 122, 200]
    a = [5, 1, 0, 122, 12, -100, 200]
    SelectionSort.selection_sorted(a)
    assert a == [-100, 0, 1, 5, 12, 122, 200]
