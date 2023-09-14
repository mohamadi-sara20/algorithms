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