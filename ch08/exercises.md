## 8.1.1
```
at least n-1 comparisons necessary --> min depth = n-1
```
## 8.1.2
```
A.11: 
∫(1, n) lgxdx <= Σ lgk <= ∫(1, n+1) lgxdx
∫(1, n) lgxdx <= Σ lgk <= ∫(1, n+1) lgxdx
nln(n) - n + 1 <= Σ lgk  <= nln(n+1) + ln(n+1) - n 
So lgk is bounded from below and above by nlg(n). 
```
## 8.1.3
```
```
## 8.1.4
```
Any sorting algorithm: nlgn
k * n/k lg(k) = nlg(k) = nlgk
```
## 8.2.1
```
C = [2,4,6,8,9,9,11]
A = [0,0,1,1,2,2,3,3,4,6,6]
```
## 8.2.2
```
```
## 8.2.3
```
It works because the order of picking does not change the correctness. 
It will not be stable though, as we put the thing we picked last first. 
```
## 8.2.4
```
Counting sort as a preprocessing step will make this happen. 
```
## 8.3.1
```
```
## 8.3.2
```
Insertion sort: stable
Merge sort: stable (better put, can be ensured stability is respected by first putting the element from he left subarray in the output array.)
Heapsort: 
Quicksort: 
```


