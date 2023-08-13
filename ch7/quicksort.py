def _quicksort(A, p, r, descending=False):
    if p < r:
        q = partition(A, p, r, descending=descending)
        _quicksort(A, p, q-1, descending=descending)
        _quicksort(A, q+1, r, descending=descending)
    return A

def partition(A, p, r, descending=False):
    x = A[r]
    i = p - 1
    j = p
    if descending: 
        while j < r:
            if A[j] >= x:
                i += 1
                tmp = A[i]
                A[i] = A[j]
                A[j] = tmp
            j += 1
        tmp = A[i+1] 
        A[i+1] = A[j] 
        A[j] = tmp
    else:
        while j < r:
            if A[j] <= x:
                i += 1
                tmp = A[i]
                A[i] = A[j]
                A[j] = tmp
            j += 1
        tmp = A[i+1] 
        A[i+1] = A[j] 
        A[j] = tmp
    return i+1

def quicksort(A, descending=False):
    if descending:
        return _quicksort(A, 0, len(A)-1, descending=True)   
    return _quicksort(A, 0, len(A)-1)
