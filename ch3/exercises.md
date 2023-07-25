# Chapter 3 Exercises & Problems

## 3.1.1
```
Prove max(f(n), g(n)) =  θ(f(n) + g(n)).

Find a c1 and a c2 so that:
c1*(f(n) + g(n)) <= max(f(n), g(n)) <= c2*(f(n) + g(n))
c1 <=  max(f(n), g(n))  / (f(n) + g(n))
c2 =>  max(f(n), g(n))  / (f(n) + g(n))

max(f(n), g(n))  / (f(n) + g(n)) is always smaller than 1. So c2 = 2 could be one example. 

c1(f(n) + g(n)) < max(f(n), g(n)), so c=1/2 could make this inequality valid, because

1/2(f(n) + g(n)) <= max(f(n), g(n)) = 
(f(n) + g(n)) <= 2max(f(n), g(n)). 

```

## 3.1.2
```
(n+a)^b = θ(n^b)

c1.n^b <= (n+a)^b <= c2.n^b

If a > 0:
c1 = 1 would hold in c1.n^b <= (n+a)^b for n0>0.
For a possible value for c2: (n+a)^b <= b/2(b+1)a^b.n^b holds for a>1 and (n+a)^b <= b/2(b+1)a.n^b holds for a<1.

If a < 0:
c1 = 1 would hold in c1.n^b <= (n+a)^b for n0>0.
For a possible value for c2: (n+a)^b <= b/2(b+1)|a|^b.n^b holds for a<-1 and (n+a)^b <= b/2(b+1)|a|^b.n^b holds for a>-1.

```


## 3.1.3
```
O is an upper bound, so it cannot tell us what the running time 'at least' is, rather 'at most'. 
```
## 3.1.4

```
Is 2^(n+1) O(2^n)? Yes, it is only by a constant factor 2 that they differ, so it's possible to find a c so that 2*2^n < c * 2^n. For example, c=3 could work here, as well as many other values. 

Is 2^(2^n) O(2^n)? 
lim 2^(2^n)  / 2^n = ∞, so  2^(2^n) is always greater than 2^n. So it cannot be θ(2^n).  
```

## 3.1.5
```
If f(n) = Ω(g(n)) and g(n) = O(g(n)), there is a constant c1 and a constant c2 such that f(n) => c1.g(n) and f(n) <= c2.g(n). So f(n) = θ(g(n))

If f(n) = θ(g(n)), then there is a c1 and c2 such that c1.g(n) <= f(n) <= c2.g(n). So we can say f(n) = O(g(n)) and f(n) = Ω(g(n)).
```

## 3.1.6
```
Upper bound: worst input upper bound
If f(n) = O(g(n)) on the worst input, it is O(g(n)) on every input. 

Lower bound: Best input lower bound
If f(n) = ω(g(n)) for the best input, it is ω(g(n)) for every input. 

So if we take the worst input for the upper bound and the best on the lower bound, we have computed the upper bound on every input and the lower bound on every input. So it is always true that f(n) = O(g(n)) and f(n) = ω(g(n)). If f(n) = O(g(n)) and f(n) = Ω(g(n)), then f(n) = θ(g(n)). 
```

## 3.1.7
```
Prove o(g(n)) ∩ ω(g(n)) is an empty set. 

o(g(n)) = {f(n): for any c > 0, there is an n0>0 such that 0<=f(n)<=cg(n)}

ω(g(n)) = {f(n): for any c > 0, there is an n0>0 such that 0<=cg(n)<=f(n)}

o(g(n)) ∩ ω(g(n)) =  functions asymptotically greater than f(n) ∩ functions asymptotically smaller than f(n) = ∅

```

## 3.1.8

```
Ω(g(n,m)) = {f(n,m): there is a + constant c,n0,m0 such that 0 <= cg(n,m) <=f(n,m)}

θ(g(n,m)) = {f(n,m): there is a + constant c,n0,m0 such that 0 <= c1g(n,m) <=f(n,m) <= c2g(n,m)}

```

## 3.2.1
```
x1 < x2 -> f(x1) < f(x2) and g(x1) < g(x2) -> f(x1) + g(x1) < f(x2) + g(x2)

x1 < x2 -> g(x1) < g(x2) -> f(g(x1)) < f(g(x2))

x1 < x2 -> f(x1) < f(x2) and g(x1) < g(x2) 
f(x) and g(x) are nonnegative -> f(x1)g(x1) < f(x2)g(x2)

```

## 3.2.2
```
a^(lgc) = c^(lga) --> lg(a^(lgc)) = lg(c^(lga)) --> lga.lgc = lgx.lga
```

## 3.2.3
```
c1.n.lgn <= lg(n!) <= c2.n.lgn
lgn! < lg(n^n) -> lgn! < nlgn -> c2=1 could be one possible value.

c1.n.lg(c1.n) < lg(n!) = lg1 + lg2 + ... + lgn
lg1 + lg2 + ... + lgn > lgn + lg(n-1) + ... + lg(n/2) > n/2 lg(n/2)
--> n/2 lg(n/2) < lg(n!) (c=1/2)

Stirling's approximation: 
lgn! = lg((2πn)^0.5 * (n/e)^n * (1+θ(1/n)))
θ(lgn!) = θ(lg((2πn)^0.5 * (n/e)^n * (1+θ(1/n)))) --> θ(lgn!) = nlgn


n!=o(n^n): lim(n!/n^n) = ∞
n! = ω(2^n): lim(2^n/n!) = 0

```
## 3.2.6
```
x^2 = 1 + x

((1+5^0.5)/2)^2 = (1 + 5 + 2*5^0.5)/4 = (6+2*5^0.5)/4
1 + (1+5^0.5)/2 = (2 +  (1+5^0.5))/2 =  (3+5^0.5)/2
So they are equal. 

((1-5^0.5)/2)^2 = (1 + 5 - 2*5^0.5)/4 = (6-2*5^0.5)/4
1 + (1-5^0.5)/2 = (2 +  (1-5^0.5))/2 =  (3-5^0.5)/2
So they are equal. 

```
## 3.2.7
```
phi = Φ
phic = the conjugate

We assume the formula is correct for l:
Fk = (phi^k - phic^k)/5^0.5 
We must prove Fk+1 equals (phi^(k+1) - phic^(k+1))/5^0.5 

Fk+1 = (phi^k - phic^k)/5^0.5 + Fk-1 
= (phi^k - phic^k)/5^0.5 + (phi^(k-1) - phic^(k-1))/5^0.5 
= (phi^k - phic^k + phi^(k-1) - phic^(k-1))/5^0.5 = (phi^(k-1)[phi + 1] - phic^(k-1)[phic + 1]) /5^0.5 = phi^(k+1) - phic^(k+1) / 5^0.5

```

## 3.2.8
```
klnk = θ(n) --> k = θ(n/lnn )

c1n <= k.lnk <= c2n
c1n/lnn <= klnk/lnn <= c2n/lnn
as n goes to infinity, k/lnn goes to zero, so c1n/lnn<=k<=c2n/lnn --> k = θ(n/lnn )

Note to self: when proving some function is θ(n/lnn), k is allowed to be taken as a constant and the only variable there is n.
```




# Problems
## 3.2 
```
lg^k(n) = o(n^eps) and O(n^eps)
n^k = O(c^n) and o(c^n)
n^0.5 and n^sinn cannot be compared in terms of growth as sin is always [-1, 1]. 
2^n = Ω((2^n)^0.5) and ((2^n)^0.5) and ω((2^n)^0.5)
n^lgc = θ(c^lgn) becaue n^lgc = (2^lgn)^lgc = c^lgn
lgn! = θ(lg(n^n)) [Stirling approximaton, p. 57]
```
## 3.3
```
1, n^(1/lgn)
lg\*lgn, lglg\*n
lg\*n
2^lg\*n
lnlnn
lgn^0.5
lnn
lg^2(n)
2^((2lgn)^0.5)
(2^0.5)^lgn
n, 2^lgn
nlgn, lg(n!)
n^2
4^lgn
n^3
n^lglgn
lg^lgn
(lgn)!
(3/2)^n
2^n
e^n
n2^n
n!
(n+1)!
2^2^n
2^2^(n+1)
```

## 3.4 
```
a. Wrong. n = O(n^2) but n^2 ≠ O(n)
b. Wrong. n+lgn ≠ O(lgn)
c. Correct. 
d. Wrong. cn = O(n), but 2^cn ≠ O(2^n) 
e. Correct for incerasing functions. For decreasing functions like 1/x, this would not be the case. 
f. Correct. 
g. Wrong. 
h. Correct. f(n) + o(f(n)) <= f(n) + f(n) = 2f(n) = θ(f(n))

```