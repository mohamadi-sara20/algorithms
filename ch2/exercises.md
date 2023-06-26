# Chapter 2 Exercises & Problems

## 2.1.1

```
(key starts at j = 2)
31, 41, 59, 26, 41, 58
31, 41, 59, 26, 41, 58
31, 41, 59, 26, 41, 58
26, 31, 41, 59, 41, 58
26, 31, 41, 41, 59, 58
26, 31, 41, 41, 58, 59
```

## 2.1.2

```
for j = 2 to A.length
    key = A[j]
    i = j - 1
    while i > 0 and A[i] < key:
        A[i] = A[j]
        i = i - 1
    A[i+1] = key
```

## 2.1.3

```
LinearSearch(v, A)
i = 0
while i < A.length:
    if v == A[i]:
        return i
    i = i + 1
return NIL

Loop Invariant: at i, v is definitely not in A[1 ... i-1].

1. Initialization: Before the first iteration, at i = 0, loop invariant is True (v has not been seen from 0 to 1)
2. Maintenance: Each iteration maintains the loop invariant, because -informally- the subarray A[i] at each iteration tells us whether or not v is in that index. If not, we increment the i and move on to the next iteration. If yes, we return. 
3. Termination: At i=A.length + 1, we are certain v does not exist in the array, and therefore return null. 
```

## 2.1.4

```
AddBinary(A, B)
for j = A.length downto 1:
    if A[j] + B[j] < 2:
        C[j] = A[j] + B[j]
    else:
        C[j] = 0
        C[j - 1 ] += 1
return C

<!-- def add(A, B):
    C = [0 for i in range(len(A)+1)]
    for j in reversed(range(len(A))):
        if A[j] + B[j] < 2:
            C[j] = A[j] + B[j]
        else:
            C[j] = 0
            C[j ] += 1
    return C -->
```

## 2.2.1

```
Θ(n^3)
```

## 2.2.2

```
Loop Invariant: 1 to k has k smallest numbers of the array in a sorted order. 
It runs only n-1 times, because by the time we reach the nth element, n-1 smallest elemnts have been sorted, and so n is the nth small element and is therefore already placed where it should be. 
Best case: Θ(n^2)
Worst case: Θ(n^2)
Best case and worst case does are the same, because it does not matter what orer the elements come in, we need to do a certain number of comparisons at each iteration anyway (to find the k smallest number), independent of the primary configuaration of the array. 
```

## 2.2.3

```
Average: E(X) = sum(pi * xi) = 1/n * sum(xi) = (n * (n + 1))/2n = (n+1)/2 (pi is equal for all indices, and xi are indices themselves)
Worst case: n elements should be checked. 
```

## 2.2.4

```
Caching could help?
```

## 2.3.1

```
            3 9 26 38 41 52 57
    3 26 41 52              9 38 49 57
3   41      26  52      38  57      9   49
3   41      52  26      38  57      9   49
```


## 2.3.2
```
See _merge_nosentinel.py_. 
```

## 2.3.3


## 2.3.4

```
See _insertion_recursive.py_. 
```

## 2.3.5

```
See _binary_search.py_. 
Binary search is Θ(lgn), because the problem is repeatedly split in half (divide), and solved from smaller to greater pieces. Since the array has n elements, it can be split in half lgn times. 


BinarySearch(A, low, high, v):
    if low <= mid:
        mid = (high + low) / 2
        if v == A[mid]:
            return mid
        if x < A[mid]:
            BinarySearch(A, low, mid, v)
        else:
            BinarySearch(A, mid+1, high, v)
```


## 2.3.6
```
Combining binary search with insertion sort would not help the performance much, because although we know where to insert the current element, the number of items to be moved remain the same as the linear search case. 
```

