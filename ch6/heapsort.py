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


def build_heap(A, loopified=False):
    if loopified:
        i = math.floor(len(A)/2)
        while i >= 0:
            heapify_loopified(A, i)
            i -= 1
    else:
        i = math.floor(len(A)/2)
        while i >= 0:
            heapify(A, i)
            i -= 1
    return A

def _heapsort(A, loopified=False):
    if loopified:
        A = build_heap(A)
        for i in range(len(A)):
            A = build_heap(A, loopified=True)
            tmp = A[len(A) - i - 1]
            A[len(A) - i - 1] = A[0]
            A[0] = tmp
            A.HEAP_SIZE -= 1
    else:
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

def heapify_loopified(A, k): 
    i = math.floor(len(A)/2)
    while k <= i:
        largest = k
        left = 2 * k + 1
        right = 2 * (k+1)
        if left < A.HEAP_SIZE and A[largest] < A[left]:
            largest = left
        if right < A.HEAP_SIZE and A[largest] < A[right]:
            largest = right
        if largest != k:
            tmp = A[largest]
            A[largest] = A[k] 
            A[k] = tmp
            k = largest
        else:
            k += 1
    return A

def heapsort_loopified(A):
    return _heapsort(HeapArray(A, len(A)), loopified=True)
