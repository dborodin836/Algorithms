# Can be upgraded by using binary search
def insertion(a_list: list):
    for i in range(1, len(a_list)):
        if a_list[i - 1] > a_list[i]:
            for j in range(0, i):
                if a_list[j] >= a_list[i]:
                    a_list.insert(j, a_list[i])
                    a_list.pop(i + 1)
