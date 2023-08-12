import math

class HeapArray(list):
    def __init__(self, A, HEAP_SIZE):
        self._HEAP_SIZE = HEAP_SIZE
        list.__init__(self, A)
    @property
    def HEAP_SIZE(self):
        return self._HEAP_SIZE
    @HEAP_SIZE.setter
    def HEAP_SIZE(self, h):
        self._HEAP_SIZE = h
    

def heapify(A, i):
    largest = i
    left = 2 * i + 1
    right = 2 * (i+1)  
    if left < A.HEAP_SIZE and A[left] > A[largest]:
        largest = left
    if right < A.HEAP_SIZE and A[right] > A[largest]: 
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
    A = build_heap(A)
    for i in range(len(A)):
        A = build_heap(A)
        tmp = A[len(A) - i - 1]
        A[len(A) - i - 1] = A[0]
        A[0] = tmp
        A.HEAP_SIZE -= 1
    return A


def heapsort(A):
    return _heapsort(HeapArray(A, len(A)))
