def bubble(a_list: list):
    for j in range(len(a_list)):
        for i in range(1, len(a_list) - j):
            if a_list[i - 1] > a_list[i]:
                a_list[i - 1], a_list[i] = a_list[i], a_list[i - 1]
