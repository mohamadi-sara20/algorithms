def binary_search(A, p, r, x):
    if p > r:
        return -1
    
    q = (r + p) // 2
    if x == A[q]:
        return q
    if x < A[q]:
        return binary_search(A, p, q-1, x)
    else:
        return binary_search(A, q+1, r, x)

if __name__ == "__main__":
    A = [1,2,3,4,5,6]
    print(binary_search(A, 0, len(A)-1, 41))
