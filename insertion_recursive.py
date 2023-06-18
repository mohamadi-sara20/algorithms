# Loop Invariant: A[0 : i-1] is always sorted
def insertion_recursive(A, i):
    if i == 0:
        return
    insertion_recursive(A, i-1)
    key = A[i]
    j = i - 1
    while j >= 0 and A[j] > key:
        A[j+1] = A[j]
        j -= 1 
    A[j+1] = key
    return A
