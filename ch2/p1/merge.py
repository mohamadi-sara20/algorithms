import math
import time
import matplotlib.pylab as plt


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

def merge_sort(A, p, r, k=10):
    if p < r:
        q = p + (r-p) // 2 
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        if r > k:
            merge(A, p, q, r)
        else: 
            insertion_sort(A)
    return A


if __name__ == "__main__":
    # a. (n/k) * k^2 = nk
    # b. n * log(n/k) (n is the length of the array that is being merged (all elements have to be seen at least once in merging) 
    # && log(n/k) is the length of the binary tree with n/k elements.)
    # c. a * lgn = lg(n/k) --> a * lgn = lgn - lg k --> -algn + lgn = lgk --> lgk = (a-1) lgn --> k = n^(1-a)
    # d. In practice, we could try out different ks for different lengths that are relevant to the use case and pick k. 
    # It seems for example that k=8 seems like a reasonable choice if length is around 100 and 1000 and k ={2, 4, ... , 1024}
    A = [i for i in range(1000, 0, -1)]
    B = [i for i in range(100, 0, -1)]
    # C = [i for i in range(10, 0, -1)]
    D = [A, B]
    # print(A)
    k = [2**k for k in range(2, 10)]
    for j in range(len(D)):
        times = dict({})
        for i in range(len(k)):
            start = time.time()
            b = merge_sort(D[j], 0, len(D[j])-1, i)
            end = time.time()
            rt = end - start
            key = str(len(D[j]))
            times[key + "k="+ str(k[i])] = rt
    
        lists = sorted(times.items())
        x, y = zip(*lists)
        plt.plot(x, y)
        plt.show()



