def bubble_sorted(a_list: list):
    for j in range(len(a_list)):
        for i in range(1, len(a_list) - j):
            if a_list[i - 1] > a_list[i]:
                a_list[i - 1], a_list[i] = a_list[i], a_list[i - 1]


def bubble(a_list: list) -> list:
    b_list = a_list[:]
    for j in range(len(b_list)):
        for i in range(1, len(b_list) - j):
            if b_list[i - 1] > b_list[i]:
                b_list[i - 1], b_list[i] = b_list[i], b_list[i - 1]
    return b_list
