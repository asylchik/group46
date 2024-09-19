def selection_sort(number_list: list):
    n = len(number_list)
    i = 0
    while i < n:
        min_number = i
        for j in range(i+1, n):
            if number_list[j] < number_list[min_number]:
                min_number = j
        number_list[i], number_list[min_number] = number_list[min_number], number_list[i]
        i += 1
    return number_list


number_list = [7, 34, 4, 9, 1]
print(selection_sort(number_list))


def binary_search(element: int, number_list: list):
    first = 0
    last = len(number_list) - 1
    result_ok = False
    pos = -1
    while first <= last:
        middle = (first + last) // 2
        if number_list[middle] == element:
            result_ok = True
            pos = middle
            break
        elif number_list[middle] < element:
            first = middle + 1
        else:
            last = middle - 1
    if result_ok:
        print(f'{element} найден на позиции {pos}')
    else:
        print('элемент не найден!')


binary_search(7, selection_sort(number_list))