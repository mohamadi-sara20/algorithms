import math
# Loop Invariant: each subarray being merged (at combine step) is sorted
# Instead of adding an Infinity to each subarray, check length when merging.  
def merge(A, p, q, r):
    L = []
    R = []
    for i in range(p, q+1):
        L.append(A[i])
    for i in range(q+1, r+1):
        R.append(A[i])
    i = 0
    j = 0
    for k in range(p, r+1):
        if i >= len(L):
            A[k] = R[j]
            j += 1
        elif j >= len(R):
            A[k] = L[i]
            i += 1
        else:
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
        
       
    return 

def merge_nosentinel(A, p, r):
    if p < r:
        q = p + (r-p) // 2 
        merge_nosentinel(A, p, q)
        merge_nosentinel(A, q+1, r)
        merge(A, p, q, r)
    return A

