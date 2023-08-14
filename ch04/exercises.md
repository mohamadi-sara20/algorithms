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
2. T(n) = 143640(n/70) + θ(n^2) is n^log(143640, 70);  n^2 <  n^log(143640, 70) so T(n) = θ(n^2.795122689748337).
3. T(n) = 155424(n/72) + θ(n^2) is n^log(155424, 72); n^2 <  n^log(155424, 72) so T(n) = θ(n^2.795147391093449)

Fastest in order:
2 > 1 > 3


4. Strassen: T(n) = 7T(n/2) + θ(n^2)
n^2 < lg7, so T(n) =  θ(n^2.81). 

Fastest in order:
2 > 1 > 3 > 4. 

```

## 4.2.6
```
a. k.1 by 1.k has k^2 multiplications. Each multiplication is a Strassen subroutine so k^2*lg7.
b. 1.k by k.1 has k multiplications. Each multiplication has a Strassen subroutine so lg7*k. 

```

## 4.2.7
```
P1 = a(d+c) = ad + ac
P2 = c(a-b) = ac - bc
P3 = d(a+b) = ad + bd
R = P1 - P3 =  ad + ac - (ad + bd) = ac - bd
I = P1 - P2 = ad + ac - (ac - bc) = ad + bc

```

## 4.3.1
```
T(n) = T(n-1) + n 
T(n) <= c(n-1)^2 + n = cn^2 + c - 2cn + n = cn^2 + c - n (2c-1) 
     <= cn^2
```

## 4.3.2
```
T(n) = T(⌈n/2⌉) + 1 
T(n) <= lg(⌈n/2⌉) + 1 = lgn - lg 2 + 1 = lgn
```

## 4.3.3
```
T(n) = 2T(⌊n/2⌋) + n
T(n) <= c.2⌊n/2⌋lg(⌊n/2⌋) + n <= cnlg(n/2) + n <= cn(lgn - lg2) + n = cnlgn - cn + n = cnlgn - n(c-1) <= cnlgn
For c > 1. So T(n) = θ(nlgn). 

T(n) >= 2c⌊n/2⌋lg(⌊n/2⌋) + n >= 2c(n/2 - 1) lg⌊n/2⌋ >= (cn - 2c) lgn/4 
= (cn-2c) (lgn - lg4) = (cn-2c) (lgn - 2) = cnlgn - 2clgn -2cn + 4c + n  = cnlgn - 2clgn + n (-2c + 1) + 4c >= nlgn if (-2c+1) > 0 that is c > 1/2. 
```

## 4.3.4
```
T(1) = 1
T(n) = 2T(⌊n/2⌋) + n 
If we prove T(n) is O(nlgn + 1), then:

T(n) <= 2 ⌊n/2⌋ lg(⌊n/2⌋) + n <= nlgn/2 + n <= nlgn - n + n = nlgn < nlgn + 1

T(1) <= 1.lg(1) + 1 = 1, so it holds. 
```

## 4.3.5
```
1. 
T(n) = T(⌈n/2⌉) + T(⌊n/2⌋) + θ(n)
T(n) <= ⌈n/2⌉lg(⌈n/2⌉) + ⌊n/2⌋ lg(⌊n/2⌋) + dn <= c.n/2lg(n/2) + c.nlg(n) + dn
<= cnlgn+cnlgn+cn = 2c.nlgn+dn <= nlgn holds for 0 < c < 1. 
2.
T(n) >= ⌈n/2⌉lg(⌈n/2⌉) + ⌊n/2⌋ lg(⌊n/2⌋) + dn >= cn/4lgn/4 + cn/4lgn/4 + dn = c/2 (nlgn/4) + dn = c/2 nlgn - cn + dn = c/2 * nlgn + n(d-c) >= nlgn for c > 2. 

So T(n)=O(nlgn) and T(n) = Ω(nlgn) --> T(n) = θ(nlgn). 
```

## 4.3.6
```
T(n) = 2(T(⌊n/2⌋) + 17) + n = O(nlgn). 

T(n) <= 2c(⌊n/2⌋+17)lg(⌊n/2⌋ +17) + n <= 2c(n/2+17)lg(n/2+17) + n 
<= 2c(n+17)lg(n+17) + n = 4cn + 4cnlgn + n <= nlgn if c < 1/4. 
```

## 4.3.7
```
T(n) = 4T(n/3)+n
T(n) <= 4(c(n/3)^lg(4,3)) + n = 4cn^lg(4,3) + n 

subtract a lower order term: n

T(n) <= 4c((n/3)^lg(4,3)-n/3) + n = 
4c(n/3)^lg(4,3) - 4cn/3 + n = 
4c(n/3)^lg(4,3) - (4cn - 3n /3) 
for c > 3/4, 4cn > 3n and so (4cn - 3n)/3 is a positive number that we are subtracting from the first term, so:
T(n) <= 4c(n/3)^lg(4,3) - (4cn - 3n /3) <= 4c(n/3)^lg(4,3) = m(n/3)^lg(4,3)
```

## 4.3.8
```
```

## 4.3.9
```
```

## 4.4.1 
```
T(n) = n + (3/2)*n + (3/2)^2 * n + ... + (3/2)^((lgn)-1)*n + 3^lgn

Sum of the first n-1 terms = n * [(3/2)^((lgn)-1) - 1]/(1/2) =>
T(n) = 2n(3/2)^((lgn)-1) - 2n + 3^lgn = O(3^lgn) = O(n^lg3)

Substitution method:
T(n) <= 3 * ⌊n^lg3/2⌋ + cn <= 3/2 * n^lg3 + cn = 3/2 * n^lg3 (1 + c/n^a) 
[a < 1, as n goes to infinity, c/n^a goes to zero] so T(n) = O(n^lg3)

```

## 4.4.2
```
recursion tree gives us: T(n) = n^2 + n^2/4 + n^2/16 + ... + n^2/4^((lg2)-1) + lgn
T(n) ≈ n^2 * 1/(1-1/4) = 4/3 * n^2
Substitution method:
T(n) <= ⌊n^2/4⌋ + cn^2 <= n^2/4 + cn^2 <= 2cn^2 --> T(n) = O(n^2)

```
## 4.4.3
```
recursion tree gives us: T(n) = n + 2n + 4n + 8n + .... + 2^(lgn)
T(n) = n * (2^lgn - 1 / (2-1)) = n * (2^lgn - 1) = n * 2^lgn - n = n*n - n = n^2 - n --> O(n^2)

Substitution method:
T(n)<= 4(n/2 + 2)^2 + n = 4(n^2/4 + 4 + n) + n = n^2 + 16 + 4n + cn <= 4n^2 + 16 + (c+4)n <= 5n^2 --> T(n) = O(n^2). 

```
## 4.4.4
```
1 + (1 + 1) + (1+1 + 1+1) + ... = 1 + 2 + 4 + ... + 2^n = O(2^n)
```

## 4.4.5
```
```

## 4.4.6
```
The cost at each depth of the tree is n. 
Depth 1: n
Depth 2: 2n/3 + n/3 = n
Depth 3: 4n/9 + 2n/9 + 2n/9 + n/9 = 9n/9 = n
.
.
.
Since the cost is always n at each level, the total number of computations is n * depth.
If we'd divide by 2 each time (equal subtrees), tree depth would be: lgn. 
Here we are dividing by 2/3 and 1/3 each time, and so the difference with the equal subtrees case is only by a constant factor. 

```

## 4.4.7
```
```
## 4.4.8
```
```
## 4.4.9
```
```

## 4.5.1 
```
a = 2
b = 4

a. 
f(n) = 1
n^lg(4, 2) =  √n 
f(n) = 1 
√n > 1 so T(n) =  θ(√n)

b. 
f(n) = √n
√n = √n so T(n) =  θ(√nlgn)

c. 
f(n) = n
√n < n and n/2 < cn for c = 1/4 so T(n) =  θ(n)

d. 
f(n) = n^2
√n < n^2 and 2(n/4)^2 = n^2/8 < n^2 for c = 1/16 so T(n) =  θ(n^2). 
```

## 4.5.2
```
T(n) = aT(n/4) + θ(n^2) < n^lg7

n^lg(a, 4) < n^lg7

If a < 49, then this algorithm works better than Strassen. 

```

## 4.5.3
```
T(n) = T(n/2) + θ(1)
f(n) = a
a = 1
b = 2 
n^lg1 = n^0 = 1

(fn) = n^lg1 --> T(n) = θ(n^0lgn) = θ(lgn) = 

```

## 4.5.4
```
It cannot. 
f(n) = n^2lgn
a = 4
b = 2
n^lg(4, 2) = n^2

n^2 is not polynomically smaller than f(n), so here we're stuck in the gap. O(n^3) could work, but there must be a tighter bound too. 

```
