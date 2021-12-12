# Can be upgraded by using binary search
def insertion_sorted(a_list: list):
    for i in range(1, len(a_list)):
        if a_list[i - 1] <= a_list[i]:
            continue
        else:
            for j in range(i, 0, -1):
                if a_list[j - 1] > a_list[i]:
                    a_list[j - 1], a_list[i] = a_list[i], a_list[j - 1]


if __name__ == '__main__':
    a = [1, 0, 0, 2, 3, 2]
    insertion_sorted(a)
    print(a)
