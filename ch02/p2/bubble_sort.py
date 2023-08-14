# Loop Invariant: Second part of the array is always sorted.
def bubble_sort(A):
    for i in range(len(A)-1):
        for j in range(1, len(A)):
            if A[j-1] > A[j]:
                tmp = A[j-1]
                A[j-1] = A[j]
                A[j] = tmp
    
    return A


# b. Initialization, Maintenance, and Termination. We need to show the loop invariant is valid before the first iteration, 
# remains valid till i= 0 to n, and when i = n +1, the array is sorted. 
# Init: At j=A.length+1, the loop invariant is zero and no part has been sorted. 
# Maintenance: At each iteration, element j is compared to element j-1 and swapped if it is smaller than j-1. 
# Termination: At j < i+1, A[i+1] contains the smallest element from [i ... A.length]. 

# c. Init: At i=0, no part of the array has been sorted yet (loop invariant equals zero). 
# Maintenance: At each i, the smallest element from [i+1...A.length] is at i+1. 
# Termination: At i=A.length -1, [0...A.length-1] is sorted, and so the last element needs not be checked. 

# d. Worst case is n^2, it is of the same order. 