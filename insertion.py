# Loop Invariant: A[0 : i-1] is always sorted
def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        # Start from the end of the loop invariant to find where to insert the new element
        j = i - 1
        # While we reach the first element and the element at hand is bigger than than A[i]
        while j >= 0 and A[j] > key:
            # Move the element at hand one to the right
            A[j+1] = A[j]
            # Go back one element in the loop invariant
            j -= 1 
        # When the element at hand (j) is not bigger than A[i], then the place to insert j is found. It is not j 
        # (because A[j] < A[i]), rather j+1. 
        A[j+1] = key
    return A
