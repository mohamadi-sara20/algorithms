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
## 6.3.1
```
A = 5, 3, 17, 10, 84, 19, 6, 22, 9
[A.length /2] = 4
build heap and heapify with i=4:

                      5
                3           17
            10     84     19   6
         22    9

                      5
                3           17
            22     84     19   6
         10    9


build heap and heapify with i=3:

                      5
                3           19
            22     84     17   6
         10    9

build heap and heapify with i=2:

                      5
                84         19
            22     3     17   6
         10    9

build heap and heapify with i=1:

                      84
                22          19
            10     3     17   6
         5    9
```
## 6.3.2
```
HEAPIFY at i assumes binary trees rooted at 2i and 2i+1 are heaps. If we increment, we cannot ensure that. We start from the lower nodes in the tree to satisfy the HEAPIFY assumption. 
```
## 6.3.3
```
At each level in the tree, the nodes are twice as many as the level before: 1 + 2^1 + 2^2 + ... + 2^l
The only level that can be not fully filled is the last level. 
The max elements of the last level (n/2) = 2 * (# all nodes in previous layers = 2^l - 1) (n/2)
# nodes in previous layers = m - 1
# max nodes in last layer = m
In that case:
m + m - 1 = n 
2m-1 = n 
max elements of the last level: n / 2
m - 1/2 = n/2
m = (n+1)/2 
Since n is odd, m = (n+1)/2 == ⌈n/2⌉
So the formula is correct for h = 0 (lowest level in the tree. )

Assume it holds for height k:
⌈n/2^(k+1)⌉
Prove it holds for height k+1, i.e. ⌈n/2^(k+2)⌉
At height k+1, the nodes are 1/2 the nodes of height k: ⌈n/2^(k+1)⌉ * 1/2 = ⌈n/2^(k+2)⌉
```
## 6.4.1
```
```
## 6.4.2
```
Initialization: At start, A[1:A.length - 1] is a max heap and A[n] has the maximum element of the whole heap. 
Maintenance: At each iteration i, A[1:A.length - i] is a max heap, because at iteration i - 1 MAX-HEAPIFY has been called on the root of the tree, so the ith greatest number of the heap is pushed up to the root of the heap. It is then swapped with n-ith element of the array and HEAPIFY then ensures that A[1:i-1] is a heap. 
Termination: When i = 1, A[2:n] is sorted and has the first maximum, second maximum, ..., n-1th maximum. It only lacks the nth maximum or the least element. A[1] has the maximum of the first part of the array, that is A[1]. It is the nth max element, in its right place. 
```
## 6.4.3
```
Increasing order: O(nlgn)
Decreasing order: O(nlgn)
```
## 6.4.4
```
BUILD HEAP is O(n). 
Worst input for the loop: Decreasing order array. Each element, when swapped, has to go down the tree O(lgn), and the loop goes from n to 2 so n-1 times. So, for the worst case, it is Ω(nlgn). 
```
## 6.5.1
```
```
## 6.5.2
```
```
## 6.5.3
```
```
## 6.5.4
```
```
## 6.5.5
```
```
## 6.5.6
```
```