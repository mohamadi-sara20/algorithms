import math
# Loop Invariant: each subarray being merged (at combine step) is sorted
def merge(A, p, q, r):
    L = []
    R = []
    for i in range(p, q+1):
        L.append(A[i])
    for i in range(q+1, r+1):
        R.append(A[i])
    R.append(math.inf)
    L.append(math.inf)
    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return 

def merge_sort(A, p, r):
    if p < r:
        q = p + (r-p) // 2 
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
    return A
