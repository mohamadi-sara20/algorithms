import math

def heapify(A, i):
    largest = i
    left = 2 * i + 1
    right = 2 * (i+1)  
    if left < HEAP_SIZE and A[left] > A[largest]:
        largest = left
    if right < HEAP_SIZE and A[right] > A[largest]: 
        largest = right
    if largest != i:
        tmp = A[largest]
        A[largest] = A[i]
        A[i] = tmp
        heapify(A, largest)
    return A


def build_heap(A):
    i = math.floor(len(A)/2)
    while i >= 0:
        heapify(A, i)
        i -= 1
    return A

def _heapsort(A):
    global HEAP_SIZE
    A = build_heap(A)
    for i in range(len(A)):
        A = build_heap(A)
        tmp = A[len(A) - i - 1]
        A[len(A) - i - 1] = A[0]
        A[0] = tmp
        HEAP_SIZE -= 1

    return A


def heapsort(A):
    global HEAP_SIZE
    HEAP_SIZE = len(A)
    return _heapsort(A)

if __name__ == "__main__":
    A = [7, 4, 5, 2, 3, 1]
    print(heapsort(A))
    
