import random
import BubleSort

if __name__ == '__main__':
    lst = [random.randint(0, 100) for i in range(250)]
    print(lst)
    selection_sorted(lst)
    print(lst)