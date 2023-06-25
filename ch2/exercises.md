# Chapter 2 Exercises

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