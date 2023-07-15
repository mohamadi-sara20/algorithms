# Horner's Rule

## a. 

```
f(n) = c1 (line 1) + c2 * n (line 2) + c3 * n (line 3) = c1 + n (c2 + c3) 
let's assume g(n) is n. So lim f(n) / g(n) when n goes to infinity =
lim ((c1 + n (c2 + c3)) / n) when n goes to infinity = c2 + c3
So we can say that f(n) ∈ θ(n).

A. 
f(n) = c1 + (c2 + c3) * n 
there is a k1 * n > f(n) 
there is a k1 > c1/n + c2 + c3
for instance, for n > 1, k1 = c1 + c2 + c3 is a possibe value. So, there is a k1 * n > f(n)

B. 
there is a k2 * n < f(n) 
there is a k2 < c1/n + c2 + c3
for instance, for n > 1, k2 = c2 + c3 is a possible value. So there's a k2 * n < f(n)
So the code fragment's complexity ∈ θ(n). 
```

## b. 
```
y = 0
p = 1
for i = n down to 0
    p = p * ai
    for j = 0 to i 
        p = x * y
    y = p + y

This is ∈ θ(n^2). This is not as efficient as Horner's rule. 
```

## c. 

```
At termination:
i = -1, so k ranges from 0 to n, i.e. y = Σ(k=0 to n) ak+1 * x^k = a1 + a2 * x + a3 * x^2 + ... + an * x*n
So the sum is correct at termination. 

Initially, when i = n, the sum is zero. 

When at iteration i, at line 2, we have the value of y from iteration i+1:

y = a_i + x * Σ(k=0 to n-(i+1)) a_k+i+1 * x^k #variabe change p = k + 1
= a_i + x * Σ(p=1 to n-i) a_p+i * x^(p-1)
= a_i + Σ(p=1 to n-i) a_p+i * x^(p+1)
= a_i + Σ(p=1 to n-i) a_p+i * x^p  (*) AND a_i = a_i+0 * x^0 (**)
(*) and (**) --> y = Σ(p=0 to n-i) a_p+i * x^p

When we go to i-1 (line 2), the value of y = y at iteration i-1.
```
