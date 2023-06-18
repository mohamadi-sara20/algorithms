# Loop Invariant: A[0 : i-1] is always sorted
def insertion_sort(A, i):
    if i == 0:
        return
    insertion_sort(A, i-1)
    key = A[i]
    j = i - 1
    while j >= 0 and A[j] > key:
        A[j+1] = A[j]
        j -= 1 
    A[j+1] = key
    return A

if __name__ == "__main__":
    A = [6,5,4,3,2,1]
    print(insertion_sort(A, len(A)-1))