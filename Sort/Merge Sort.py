def merge_sort(unsorted):
    if len(unsorted) <= 1:
        return unsorted

    mid = len(unsorted) // 2
    left = unsorted[:mid]
    right = unsorted[mid:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge(sorted_left, sorted_right)


def merge(left, right):
    i = 0
    j = 0
    sorted_list = []

    while (i < len(left)) & (j < len(right)):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    while (i < len(left)):
        sorted_list.append(left[i])
        i += 1

    while (j < len(right)):
        sorted_list.append(right[j])
        j += 1

    return sorted_list

print(merge_sort([1,7,3,45,77,33,7,4]))