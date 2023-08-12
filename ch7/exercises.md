## 7.1.1
```
A = 13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11
(1) i=0, p=1, j=1: 13 > 11; j++
(2) i=0, p=1, j=2: 19 > 11; j++
(3) i=0, p=1, j=3: 9 < 11; i++ and exchange A[1] with A[3] so A = 9, 19, 13, 5, 12, 8, 7, 4, 21, 2, 6, 11 and j++
(4) i=1, p=1, j=4: 5 < 11; i++ and exchange A[2] with A[4] so A = 9, 5, 13, 19, 12, 8, 7, 4, 21, 2, 6, 11 and j++ 
(5) i=2, p=1, j=5: 12 > 11; j++
(6) i=2, p=1, j=6: 8 < 11; i++ and exchange A[3] with A[6] so A = 9, 5, 8, 19, 12, 13, 7, 4, 21, 2, 6, 11 and j++ 
(7) i=3, p=1, j=7: 7 < 11; i++ and exchange A[4] with A[7] so A = 9, 5, 8, 7, 12, 13, 19, 4, 21, 2, 6, 11 and j++ 
(8) i=4, p=1, j=8: 4 < 11; i++ and exchange A[5] with A[8] so A = 9, 5, 8, 7, 4, 13, 19, 12, 21, 2, 6, 11 and j++ 
(9) i=5, p=1, j=9: 21 > 11; j++
(10) i=5, p=1, j=10: 2 < 11; i++ and exchange A[6] with A[10] so A =  9, 5, 8, 7, 4, 2, 19, 12, 21, 13, 6, 11 and j++ 
(10) i=6, p=1, j=11: 6 < 11; i++ and exchange A[7] with A[11] so A =  9, 5, 8, 7, 4, 2, 6, 12, 21, 13, 19, 11 and j++ 
(11) swap A[i+1] with A[r] so A =  9, 5, 8, 7, 4, 2, 6, 11, 12, 21, 13, 19
```
## 7.1.2
```
r (We do i++ r-1 times and at the end we r-1+1, so i = r). 
```
## 7.1.3
```
We compare each element to the pivot only once, so r-1-p comparisons are made, and the rest is constant O(1). r-1-p is proportional to the size of the array, so it is Θ(n).
```
## 7.1.4
```
line 4 should be changed to A[j] >= x. 
```
## 7.2.1
```
(a) T(n) <= (n-1)^2 + Θ(n) = n^2 + 1 - 2n + Θ(n) <= 2n^2 so T(n) = O(n^2)
(b) T(n) >= (n-1)^2 + Θ(n) = n^2 + 1 - 2n + Θ(n) > n^2/2 so T(n) = Ω(n^2)
From (a) and (b): T(n) = Θ(n^2)
```
## 7.2.2
```
All equal elements: 
First time, q = r, and we will have a n-1 to 1 partition. 
Second time, q = r, and we will have a n-1 to 1 partition. 
And so son. Each time, the q equals r, and we have p to q-1 and q-q partitions, which is a n-1 to 1 ratio: the worst case. It can be described with the recurrence relation above: T(n) = T(n-1) + + Θ(n), which is Θ(n^2), as shown. 
```
## 7.2.3
```
In this case too, we always have a n-1 to 1 ratio, so the reccurence would again be (n) = T(n-1) + + Θ(n). Because the first time, q = r. Second time, q = r again, and so on. So this case is also a 'worst case'. 
```
## 7.2.4
```
Insertion sort's performance on almost sorted data is O(n), while almost sorted input could take the shape of T(n) = T(n-c) + Θ(n) for quicksort, which is Θ(n^2). 
```
## 7.2.5
```
```



