def quicksort(arr, lo, hi):
    def partition(lo, hi):
        pivot = arr[hi]
        left = lo

        for right in range(lo,hi):
            if arr[right] < pivot:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1

        arr[left], arr[hi] = arr[hi], arr[left]

        return left

    if lo < hi:
        pivot = partition(lo, hi)
        quicksort(arr, lo, pivot-1)
        quicksort(arr, pivot+1, hi)

    return arr

def mergesort(unsorted):
    def merge(L, R):
        i = 0
        j = 0
        sorted = []
        while i<len(L) and j<len(R):
            if L[i] < R[j]:
                sorted.append(L[i])
                i += 1
            else:
                sorted.append(R[j])
                j += 1

        while i<len(L):
            sorted.append(L[i])
            i += 1
        while j<len(R):
            sorted.append(R[j])
            j += 1

        return sorted

    if len(unsorted)==1:
        return unsorted

    mid = len(unsorted)//2
    left = mergesort(unsorted[:mid])
    right = mergesort(unsorted[mid:])

    return merge(left,right)

def binary_search(arr, left, right, target):
    mid = left + (right-left)//2

    if arr[mid] < target:
        return binary_search(arr, mid+1, right, target)
    elif arr[mid] > target:
        return binary_search(arr, left, mid-1, target)
    else:
        return mid


array = [9,1,6,2,7,8]
print(quicksort(array, 0, len(array)-1))
print(mergesort(array))
print(binary_search(array, 0, len(array)-1, 6))
