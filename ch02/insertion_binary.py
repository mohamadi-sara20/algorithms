def binary_search(A, p, r, x):
    if p > r:
        return p
    q = (r + p) // 2
    if x == A[q]:
        return q
    if x < A[q]:
        return binary_search(A, p, q-1, x)
    else:
        return binary_search(A, q+1, r, x)

# Loop Invariant: A[0 : i-1] is always sorted
def insertion_binary(A):
    for i in range(1, len(A)):
        key = A[i]
        ind = binary_search(A, 0, i-1, key)
        j = i - 1
        while j >= ind:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A
