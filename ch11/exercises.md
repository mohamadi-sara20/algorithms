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
