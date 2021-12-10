import random


def selection_sorted(a_list: list):
    for i in range(len(a_list)):
        tmp_pos = 0
        for j in range(1, len(a_list) - i):
            if a_list[j] > a_list[tmp_pos]:
                tmp_pos = j
        a_list[len(a_list) - i - 1], a_list[tmp_pos] = a_list[tmp_pos], a_list[len(a_list) - i - 1]


if __name__ == '__main__':
    lst = [random.randint(0, 100) for i in range(250)]
    print(lst)
    selection_sorted(lst)
    print(lst)
