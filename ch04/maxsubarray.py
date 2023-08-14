import math
from itertools import chain
import time
import pandas as pd
import matplotlib.pyplot as plt
import random

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

def run(input, mode='bruteforce'):
    if mode == 'bruteforce':
        start_A = time.time()
        maxsubarray_bruteforce(input)
        end_A = time.time()
        return end_A - start_A
    elif mode == 'recursive':
        start_A = time.time()
        maxsubarray(input, 0, len(input)-1)
        end_A = time.time()
        return end_A - start_A
    else:
        start_A = time.time()
        maxsubarray_bfbase(input, 0, len(input)-1)
        end_A = time.time()
        return end_A - start_A


def maxsubarray_bfbase(A, low, high):
    if high - low < 11:
        return maxsubarray_bruteforce(A)
    mid = (high + low) // 2
    low_left, high_left, max_left = maxsubarray_bfbase(A, low, mid)
    low_right, high_right, max_right = maxsubarray_bfbase(A, mid+1, high)
    low_cross, high_cross, max_cross = find_max_crossing_subarray(A, low, mid, high)
    if max_left >= max_right and max_left >= max_cross:
        return low_left, high_left, max_left
    elif max_right >= max_left and max_right >= max_cross:
        return low_right, high_right, max_right
    return low_cross, high_cross, max_cross


def maxsubarray_kadane(A):
    max_iend = A[0]
    max_sofar = A[0]
    bind = 0
    eind = 0
    bind_sofar = 0
    eind_sofar = 0
    for i in range(1, len(A)):
        if A[i] > max_iend + A[i]:
            bind = i
            eind = i
            max_iend = A[i]
        elif A[i] < max_iend + A[i]:
            eind = i
            max_iend += A[i]
        if max_iend > max_sofar:
            max_sofar = max_iend
            bind_sofar = bind
            eind_sofar = eind
        
    return bind_sofar, eind_sofar, max_sofar
    
if __name__ == "__main__":
    A = [-1, 2, 4, -3, 5, -6]
    B = [A for i in range(16)]
    C = [A for i in range(64)]
    D = [A for i in range(256)]
    E = [A for i in range(1024)]
    F = [A for i in range(4096)]
    B = list(chain.from_iterable(B))
    C = list(chain.from_iterable(C))
    D = list(chain.from_iterable(D))
    E = list(chain.from_iterable(E))
    F = list(chain.from_iterable(F))

    random.shuffle(B)
    random.shuffle(C)
    random.shuffle(D)
    random.shuffle(E)
    random.shuffle(F)

    inputs = [A, B, C, D, E, F]
    running_times_bf = {}
    running_times_recursive = {}
    for inp in inputs:
        rtb = run(mode='bruteforce', input=inp)
        rtr = run(mode='recursive', input=inp)
        running_times_bf[f'{len(inp)}'] = rtb
        running_times_recursive[f'{len(inp)}'] = rtr

    combined = {}
    for k in running_times_recursive:
        combined[k] = [running_times_recursive[k], running_times_bf[k]]
    
    running_times_recursivebfbase = {}
    for inp in inputs:
        rtb = run(input=inp)
        running_times_recursivebfbase[f'{len(inp)}'] = rtb


    print(running_times_recursivebfbase)
    print(running_times_recursive)
    print(running_times_bf)


