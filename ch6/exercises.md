## 6.1.1
```
minimum: 2^h
maximum: 2^(h+1) - 1
```
## 6.1.2
```
2^h <= n <= 2^(h+1)-1 < 2^(h+1)
h*lg2 <= lgn < (h+1)*lg2
h <= lgn < h+1
⌊lgn⌋ = h 
```
## 6.1.3
```
This is the definition of a heap, so the parent in any subtree has to be greater than its children.
```
## 6.1.4
```
The smallest value happens at the bottom of the tree in the leaves. (From the ⌊n/2⌋ + 1th element in the array.)
```
## 6.1.5
```
Yes, it is. 
```
## 6.1.6
```
No, heap constraint is violated when 6 is smaller than 7. 

                   23
            17          14
        6       13     10   1
      5   7   12
```
## 6.1.7
```
Children of node i are at 2i and 2i+1. n is the last element that can be child. 
If it is the left child (n mod 2 == 0): (a) n = 2i --> n/2 = i
If it is the right child (n mod 2 == 1): (b) n = 2i + 1 --> n/2 - 1/2 = i --> ⌊n/2⌋ = i 
⌊n/2⌋ is the last element that can be a parent, so any element after it is a leaf. So elements from ⌊n/2⌋ + 1 onwards are children. 
```
## 6.2.1
```

                 27
        17              3
   16        13     10       1
5    7    12   4   8  9    0


largest ≠ i  (largest = 2i) , so we swap and call heapfiy on largest subtree.


                 27
        17              10
   16        13     3       1
5    7    12   4   8  9    0

larges ≠ i (largest = 2i+1 or 9), so we swap and call heapfiy on largest subtree.

                 27
        17              10
   16        13     9       1
5    7    12   4   8  3    0

```
## 6.2.2
```
MIN-HEAPIFY(A, i)

left = 2i
right = 2i+1
smallest = i

if left < A.heapsize and A[smallest] > A[left]:
        smallest = left
if right < A.heapsize and A[smallest] > A[right]:
        smallest = right
if smallest ≠ i:
        swap A[i] and A[smallest]
        MINHIPIFY(A, smallest)

It is also O(lgn) (T(n) <= T(2n/3) + Θ(1)). 
```
## 6.2.3
```
Nothing, because in that case MAX-HEAPFIY will not call itself on its subtree.
```
## 6.2.4
```
Nothing, it will try to heapify children nodes, where the heap condition cannot be violated, as they have no children. 
```
## 6.2.5
```
See heapify_loopified method in heapsort.py
```
## 6.2.6
```
T(n) = T(2n/3) + Θ(1) is Ω(lgn). 
T(n) <= lg(2n/3) + Θ(1) = lg2 + lgn - lg3 + Θ(1) <= 2lgn
```