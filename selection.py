# Loop Invariant: A[:i]
def selection_sort(A):
    for i in range(len(A)):
        ind_smallest = i
        for j in range(i+1, len(A)):
            if A[j] < A[ind_smallest]:
                ind_smallest = j
        tmp = A[i]
        A[i] = A[ind_smallest]
        A[ind_smallest] = tmp
    return A

