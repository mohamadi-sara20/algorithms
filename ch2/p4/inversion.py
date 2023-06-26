import math
# Loop Invariant: each subarray being merged (at combine step) is sorted
def merge(A, p, q, r):
    c = 0
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
            # sanity check - removed for readability
            # if R[j] == math.inf:
            #     c += r - q - j 
            #     print("#####", r - q - j )
        else:
            A[k] = R[j]
            j += 1
            c += q + 1 - p - i 
    return c

def count_inversions(A, p, r):
    c = 0
    if p < r:
        q = p + (r-p) // 2 
        c += count_inversions(A, p, q)
        c += count_inversions(A, q+1, r)
        c += merge(A, p, q, r)
    return c

# a. (8, 6) (6, 1) (3, 1) (2, 1) (8, 1)
# b. The reversed order has the most inversions. #inversions = sum(i from 0 to n-1) = (n * (n-1)) / 2
# c. The inversions define the number of times we have to move the elements. 
# d. the code to count inversions in an array is above. The idea is, the inversion takes place
#   when something in the left array is bigger than some element in the right array. So it's only in this case (the else block)
#   we increment c. How much do we need to add? The length of the left array (q-p+1) minus the elements in the left subarray that were
#   smaller than the right subarray elements so far (i), hence q-p+1-i. 

if __name__ == "__main__":
    A = [6,5,4,3,2,1]
    a = count_inversions(A, 0, len(A)-1)
    print(a)