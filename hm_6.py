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
    sorted_list = selection_sort(number_list)
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == element:
            return mid
        elif sorted_list[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    return -1


print(binary_search(7, number_list))