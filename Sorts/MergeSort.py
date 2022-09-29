def merge(a_list: list, b_list: list) -> list:
    result = list()
    while a_list and b_list:
        if a_list[0] <= b_list[0]:
            result.append(a_list.pop(0))
        else:
            result.append(b_list.pop(0))
    result.extend(a_list) if a_list else result.extend(b_list)
    return result


def merge_sort(input_lst):
    if len(input_lst) > 1:

        middle = len(input_lst) // 2

        left = input_lst[:middle]
        right = input_lst[middle:]

        merge_sort(left)
        merge_sort(right)

        left_index = right_index = input_lst_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                input_lst[input_lst_index] = left[left_index]
                left_index += 1
            else:
                input_lst[input_lst_index] = right[right_index]
                right_index += 1
            input_lst_index += 1

        while left_index < len(left):
            input_lst[input_lst_index] = left[left_index]
            left_index += 1
            input_lst_index += 1

        while right_index < len(right):
            input_lst[input_lst_index] = right[right_index]
            right_index += 1
            input_lst_index += 1
