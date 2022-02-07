def bubblesort(A):
    for i in range(1, len(A)):
        for j in range(0, len(A)-i):
            if A[j]>A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
    return A

a = [4,65]
print(bubblesort(a))