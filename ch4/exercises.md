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
strassen(A, B):
    n = A.rows
    if n == 1:
        c11 = a11.b11

    else:
        split A and B and C into 4 submatrices
        compute S1, S2, ..., S10
        strassen(A11, S1)
        .
        .
        .
        strassen(S9, S10)
        c11 = P4 + P5 - P2 + P6
        c12 = P1 + P2
        c21 = P3 + P4
        c22 = P5 + P1 - P3 - P7
    return C

```

## 4.2.3
```
Padding with zeros so that the input becomes a power of two. 
Laderman has found a way to multiply odd matrices using 23 multiplications. 
```

## 4.2.4
```
n = 3^x
T(n) = kT(n/3) + θ(n^2)
n^2 = n^log(k, 3)
2 = log(k, 3) --> k = 9

If k > 9 :
-> log(k, 3) < 2.81. 
-> log(22, 3) = 2.814
-> log(21, 3) < 2.814

So if k = 21, T(n) = o(n^lg7). 

If k < 9, then T(n) =  θ(n^2) and so T(n) = o(n^lg7). 

```

## 4.2.5

```

1. T(n) = 132464T(n/68) + θ(n^2); n^2 < n^log(132464, 68) so T(n) = θ(n^2.7951284873613815).
2. T(n) = 143640(n/70) + θ(n^2) is n^log(143640, 70);  θ(n^2) <  n^log(143640, 70) so T(n) = θ(n^2.795122689748337).
3. T(n) = 155424(n/72) + θ(n^2) is n^log(155424, 72); θ(n^2) <  n^log(155424, 72) so T(n) = θ(n^2.795147391093449)

2 > 1 > 3


4. Strassen: T(n) = 7T(n/2) + θ(n^2)
n^2 < lg7, so T(n) =  θ(n^2.81). 

2 > 1 > 3 > 4. 

```

## 4.2.6

```

```

## 4.2.7
```

```
