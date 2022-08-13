def merge_w_methods(a_list: list, b_list: list) -> list:
    result = list()
    while a_list and b_list:
        if a_list[0] <= b_list[0]:
            result.append(a_list.pop(0))
        else:
            result.append(b_list.pop(0))
    result.extend(a_list) if a_list else result.extend(b_list)
    return result


def merge_wo_methods(arr: list, a_list: list, b_list: list):
    """
    :param arr: where save result
    :param a_list: first array to merge
    :param b_list: second array to merge
    :return: merged arrays at arr
    """
    # l - index of left array
    # r - index of right array
    # f - index of final array
    l = r = f = 0

    while l < len(a_list) and r < len(b_list):
        if a_list[l] < b_list[r]:
            arr[f] = a_list[l]
            l += 1

        else:
            arr[f] = b_list[r]
            r += 1
        f += 1

    while l < len(a_list):
        arr[f] = a_list[l]
        l += 1
        f += 1

    while r < len(b_list):
        arr[f] = b_list[r]
        r += 1
        f += 1


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        merge_wo_methods(arr, L, R)
