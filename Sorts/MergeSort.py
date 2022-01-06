def merge(a_list: list, b_list: list) -> list:
    result = list()
    while a_list and b_list:
        if a_list[0] <= b_list[0]:
            result.append(a_list.pop(0))
        else:
            result.append(b_list.pop(0))
    result.extend(a_list) if a_list else result.extend(b_list)
    return result
