## 11.1.1
```
Keep the max in a variable and update it whenever you see anything greater than the current max. This procedure is O(m). 
```
## 11.1.2
```
If element i exists in the dynamic set, make the ith index of the vector 1. 
SEARCH: return the ith index
INSERT: return the ith index
DELETE: make the ith index 0
```
## 11.1.3
```
An m element table. Each element in the table can be a doubly linked list. 

INSERT(T, x):
    if T[x.key] == NIL:
        T[x.key] = x
    else:
        T[x.key].next = x
        T[x.key].next.prev = T[x.key]

DELETE(T, x):
    y = T[x.key]
    while T[x.key] ≠ x:
        y = T[x.key].next
    T[x.key].y.prev.next = T[x.key].y.next
    T[x.key].y.next.prev = T[x.key].y.prev

SEARCH(T, k):
    # Just return the first element at index k
    return T[k].head
```

## 11.2.1
```
(Similar to the Birthday Problem. 
Look here: https://math.stackexchange.com/questions/35791/birthday-problem-expected-number-of-collisions
Also here: https://courses.cs.duke.edu/cps102/spring09/Lectures/L-18.pdf)
```
## 11.2.3
```
[0,(28,19,10),(20),(12),0,(5),(15,33),0,(17)]
```
## 11.2.4
```
If we are allowed to use dynamic arrays to handle collisions, search (successful and unsuccesful) can be done via binary search: Θ(1+lg(α)), and insertion and deletion: Θ(1+n) because when adding an element or deleting one, everything after that element has to be shifted one step. 
However, if we are only able to handle collision by linked lists, we cannot use a binary search to reduce running time logarithmically. Searching (successsful or unsuccessful) would still take Θ(1+α), because we cannot jump in a linked list. We can only move to the next item. 
```
## 11.3.1
```
First check hash values. If hash values are equal, we have either found our element, or one that collides with it. If hash values are the same, check the strings. 
```
## 11.3.2
```
h(61) = [1000(0.618033 * 61 mod 1)] = [1000(0.700)] = 700
h(62) = [1000(0.618033 * 62 mod 1)] = [1000(0.318046)] = 318
h(63) = [1000(0.618033 * 63 mod 1)] = [1000(0.93607900000001)] = 936
and so on...
```
## 11.4.1
```
linear probing, m = 11 & h'(k) = k:
22, 88, null, null, 4, 15, 28, 17, 59, 31, 10
h(10) = 10 (empty so no problem)
h(22) = 0 (empty so no problem)
h(31) = 9 (empty so no problem)
h(4) = 4 (empty so no problem)
h(15) = 4 (collision; add 1 to i) --> h(15) = 15 + 1 mod 11 = 5 
and so on...
```
## 11.4.2
```
procedure HASH-DELETE(T, k)
    j = HASH-SEARCH(T, k)
    T[j] = DELETED
procedure HASH-INSERT(T, k)
    i=0
    repeat
        j = h(k, i)
        if T[j] == NIL or T[j] == DELETED:
           T[j] = k
           return j
        else i = i + 1
    until i == m
    error "hash table overflow"
```