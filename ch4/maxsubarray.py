import math

def maxsubarray_bruteforce(A):
    b = 0
    e = 0
    max_sum = A[0]
    for i in range(len(A)):
        sumib = A[i]
        for j in range(i+1, len(A)):
            if i == j:
                continue
            sumib += A[j]
            if sumib > max_sum:
                b = i
                e = j
                max_sum = sumib
    return b, e, max_sum



def maxsubarray_dandc(A):
    return



def find_max_crossing_subarray(A, low, mid, high):
    left_sum = -math.inf
    right_sum = -math.inf
    max_left = mid
    max_right = mid
    j = mid
    current_sum = 0
    while j >= low:
        current_sum += A[j]
        if current_sum > left_sum:
            left_sum = current_sum
            max_left = j
        j = j - 1
    current_sum = 0
    for i in range(mid+1, high + 1, 1):
        current_sum += A[i]
        if current_sum > right_sum:
            right_sum = current_sum
            max_right = i
    return max_left, max_right, right_sum+left_sum


def maxsubarray(A, low, high):
    if high == low:
        return low, high, A[low]
    mid = (high + low) // 2
    low_left, high_left, max_left = maxsubarray(A, low, mid)
    low_right, high_right, max_right = maxsubarray(A, mid+1, high)
    low_cross, high_cross, max_cross = find_max_crossing_subarray(A, low, mid, high)
    if max_left >= max_right and max_left >= max_cross:
        return low_left, high_left, max_left
    elif max_right >= max_left and max_right >= max_cross:
        return low_right, high_right, max_right
    return low_cross, high_cross, max_cross

if __name__ == "__main__":
    
    print(maxsubarray_bruteforce(a))
    print(maxsubarray_bruteforce(b))
    print(maxsubarray_bruteforce(c))
    print(maxsubarray(a, 0, len(a)-1))
    print(maxsubarray(b, 0, len(b)-1))
    print(maxsubarray(c, 0, len(c)-1))