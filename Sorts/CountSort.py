# Probably should separate this functions into smaller ones.
# Probably not the best architecture decision.


def count(a_list: list):
    min_value = min(a_list)
    below_zero = list([0] * abs(min(a_list)))
    above_zero_and_zero = list([0] * ((max(a_list)) + 1))

    for element in a_list:
        if element >= 0:
            above_zero_and_zero[element] += 1
        else:
            below_zero[-abs(element)] += 1

    # I have a bad feeling about that.
    a_list.clear()

    for number, amount in zip(list(range(1, (abs(min_value) + 1))), below_zero[::-1]):
        a_list.extend([-number for _ in range(amount)])
    for number, amount in enumerate(above_zero_and_zero):
        a_list.extend([number for _ in range(amount)])


def count_dict(a_list: list):
    dictionary = dict()

    for element in a_list:
        if element not in dictionary:
            dictionary[element] = 0
        dictionary[element] += 1

    a_list.clear()

    for key in sorted(dictionary.keys()):
        for times in range(dictionary[key]):
            a_list.append(key)
