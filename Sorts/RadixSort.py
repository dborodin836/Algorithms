def radixLSD(a_list: list):
    a_list = list(map(str, a_list))
    for i in range(len(a_list[0])):
        a_list.sort(key=lambda x: x[-i])


if __name__ == '__main__':
    a = [0, -1, 2, 12, 5, 123, 31]
    radixLSD(a)
    print(a)
