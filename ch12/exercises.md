## 12.1.1
```
h=2:

     10
  4      17
1   5   16  21

h=3:

            16
      5         17
    4    10  nil    21
  1  nil


h=4:
            17
       16        21
    5    nil  
  4  10
1

h=5:
            17
        16      21
     10    nil  
    5    nil
  4    nil
1   nil

h=6:
    1
nil         4
       nil      5
            nil       10
                  nil      16
                        nil     17
                             nil    21

```

## 12.1.2
```
Binary Search Tree ensures left child is smaller than or equal to its parent, and parent is smaller than or equal to the right child. This is not ensured in a heap. Heap only guarantees that the parent is greater than its children. 
```
## 12.1.3
```
IN-ORDER-TREE-WALK(x):
    S = [x]
    while not S.isEmpty():
        top = S.pop()
        if top.left == nil and top.right == nil:
            print top.key
        S.push(top.right)
        newNode = Node(key=top.key, left=nil, right=nil, parent=nil)
        S.push(newNode)
        S.push(top.left)  
```
## 12.1.4
```
PRE-ORDER-TREE-WALK(x):
    if x ≠ nil:
        print x.key
        PRE-ORDER-TREE-WALK(x.left)
        PRE-ORDER-TREE-WALK(x.right)

POST-ORDER-TREE-WALK(x):
    if x ≠ nil:
        POST-ORDER-TREE-WALK(x.left)
        POST-ORDER-TREE-WALK(x.right)
        print x.key
```
## 12.1.5
```
```
## 12.2.1
```
c: From 911 onwards, everything must be smaller than or equal to 911. 912 is greater than 911. BST condition is violated. 
e: From 347 onwards, everything must be greater than or equal to 347. 199 isn't. BST condition violated. 
```

## 12.2.2
```
tree_min(x):
    if x.left == NIL:
        return x
    if x.left ≠ NIL:
        x = x.left
        return tree_min(x)

tree_max(x):
    if x.right == NIL:
        return x
    if x.left ≠ NIL:
        x = x.right
        return tree_max(x)
```
## 12.2.3
```
tree_predecessor(x):
    if x.left == Nil:
        return tree_max(x.left)
    y = x.p
    while y ≠ Nil and x == y.left:
        x = y
        y = y.p
    return y 
```

## 12.2.4
```
            7
      5         10
    4   6     9     12

If we look for 5, the search path: 7 --> 5 (B)
Left: 4, 6 (A)
Right: 9, 10, 12 (C)
6 is not smaller than 7. 
```
## 12.2.5
```
Two children --> left child and right child 
Successor: min right subtree
Predecessor: max left subtree
```
## 12.2.6
```

```
## 12.2.7
```
```
## 12.2.8
```
```
## 12.2.9
```
```

## 12.3.1
```
TREE-INSERT(T, z, p)
    if T == Nil:
        z.p = p
        if p.key < z.key:
            p.right = z
        else:
            p.left = z 
    else:
        if z.key < T.key:
            TREE-INSERT(T.left, z, T)
        else:
            TREE-INSERT(T.right, z, T)
```
## 12.3.2
```
When inserting z, a path is traversed to find the right place for it. Let's assume this path has length x. 
When looking for element z, the same path is again traversed, however, to return the value, the node inserted has to also be seen (+1). So we go through the same path + the node inserted --> x + 1
```
## 12.3.3
```
Worst Case: Linear order of nodes --> 0 (height traversed to insert the first node) + 1 + 2 + ... + (n-1) = (n-1)(n-2) / 2 = O(n^2)
Best case: balanced --> lgn height traversed for all the n nodes: O(nlgn)
```
## 12.3.4
```
```
## 12.3.5
```
```