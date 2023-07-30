# Chapter 4 Exercises & Problems

## 4.1.1
```
The least negative element.
```

## 4.1.2
```
max-sum = 0
b = 0
e = 0
for i = 1 to A.length:
    sum-i-b = A[i]
    for j = i+1 to A.length:
        sum-i-b += A[j] 
        if max-sum < sum-i-b:
            max-sum = sum-i-b
            b = i 
            e = j     
```

## 4.1.4

```

Lines 7-9, p. 72, another condition can be checked to make sure that the max is positive. If not, we can return 0. 

```

## 4.1.5
```
maxsubarray_kadane function 
```

## 4.2.1
```
C11 = 
C21 = 
C21 = 
C22 = 
```


## 4.2.2
```
n = A.rows
if n == 1:
    c11 = a11.b11

else:
    split A and B and C into 4 submatrices
    compute S1, S2, ..., S10
    compute P1, P2, ..., P7
    c11 = P4 + P5 - P2 + P6
    c12 = P1 + P2
    c21 = P3 + P4
    c22 = P5 + P1 - P3 - P7
return C


```