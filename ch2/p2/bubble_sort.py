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

# b. 