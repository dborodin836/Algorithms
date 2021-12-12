# Can be upgraded by using binary search
def insertion_sorted(a_list: list):
    for i in range(1, len(a_list)):
        if a_list[i - 1] > a_list[i]:
            for j in range(0, i):
                if a_list[j] >= a_list[i]:
                    a_list.insert(j, a_list[i])
                    a_list.pop(i + 1)


def insertion(a_list: list) -> list:
    b_list = list(a_list)
    for i in range(1, len(b_list)):
        if b_list[i - 1] > b_list[i]:
            for j in range(0, i):
                if b_list[j] >= b_list[i]:
                    b_list.insert(j, b_list[i])
                    b_list.pop(i + 1)
    return b_list
