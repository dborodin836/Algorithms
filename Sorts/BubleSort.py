def bubble(a_list: list):
    swapped = True
    while swapped:
        swapped = False
        for j in range(len(a_list)):
            for i in range(1, len(a_list) - j):
                if a_list[i - 1] > a_list[i]:
                    a_list[i - 1], a_list[i] = a_list[i], a_list[i - 1]
                    swapped = True
