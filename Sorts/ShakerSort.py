def shaker(a_list: list):
    start = 0
    end = len(a_list)
    swapped = True
    while swapped:

        swapped = False
        for j in range(len(a_list)):

            for i in range(1, len(a_list) - j):

                if a_list[i - 1] > a_list[i]:
                    a_list[i - 1], a_list[i] = a_list[i], a_list[i - 1]
                    swapped = True

            for k in range(end - j - 1 - 1, start + j + 1, -1):

                if a_list[k] < a_list[k - 1]:
                    a_list[k], a_list[k - 1] = a_list[k - 1], a_list[k]
                    swapped = True
