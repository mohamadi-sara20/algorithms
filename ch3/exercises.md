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

## 3.1.4
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

So if we take the worst input for the upper bound and the best on the lower bound, we have computed the upper bound on every input and the lower bound on every input. So it is always true that f(n) = O(g(n)) and f(n) = ω(g(n)). If f(n) = O(g(n)) and f(n) = ω(g(n)), then θ(g(n)). 
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