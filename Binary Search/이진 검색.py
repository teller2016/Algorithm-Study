a = [1, 2, 5, 6, 7, 8, 10]


def bisect(arr, left, right, target):
    mid = left + (right - left) // 2

    if arr[mid] < target:
        return bisect(arr, mid + 1, right, target)
    elif arr[mid] > target:
        return bisect(arr, left, mid + 1, target)
    else:
        return mid


print(bisect(a, 0, len(a) - 1, 10))


# bisect
import bisect
print(bisect.bisect_left(a,5))