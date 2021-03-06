def quicksort(A, lo, hi):
    def partition(lo, hi):
        pivot = A[hi]
        left = lo  # pivot보다 작은 값 옮길 위치

        for right in range(lo, hi):
            if A[right] < pivot:
                A[left], A[right] = A[right], A[left]
                left += 1

        A[left], A[hi] = A[hi], A[left]
        return left

    if lo < hi:
        pivot = partition(lo, hi)
        quicksort(A, lo, pivot - 1)         # pivot 값은 정렬된 위치에 지정되기에 pivot-1 까지하면 된다
        quicksort(A, pivot + 1, hi)

    return A


a = [4, 6, 2, 7, 1, 4, 6, 2]
print(quicksort(a, 0, len(a) - 1))
