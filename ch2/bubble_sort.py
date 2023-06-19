# Loop Invariant: Second part of the array is always sorted.
def bubble_sort(A):
    for i in range(len(A)-1):
        for j in range(1, len(A)):
            if A[j-1] > A[j]:
                tmp = A[j-1]
                A[j-1] = A[j]
                A[j] = tmp
    
    return A
