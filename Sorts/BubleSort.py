import random


def bubble_sorted(a_list: list):
    for j in range(len(a_list)):
        for i in range(1, len(a_list) - j):
            if a_list[i - 1] > a_list[i]:
                a_list[i - 1], a_list[i] = a_list[i], a_list[i - 1]


if __name__ == '__main__':
    lst = [random.randint(0, 100) for i in range(250)]
    print(lst)
    bubble_sorted(lst)
    print(lst)
